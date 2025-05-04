import pandas as pd
import mysql.connector
import joblib
import numpy as np

# Load the consumer behavior model
model = joblib.load('models/consumer_model.pkl')

# Functions from dynamic_pricing.py
def demand(price, comp_price):
    return max(0, 100 - 2 * price + comp_price)

def optimize_price(comp_price):
    prices = np.arange(10, 100, 5)
    best_price, max_revenue = 0, 0
    for p in prices:
        q = demand(p, comp_price)
        revenue = p * q
        if revenue > max_revenue:
            max_revenue, best_price = revenue, p
    return best_price, max_revenue

def dynamic_price(comp_price, customer_features):
    base_price, _ = optimize_price(comp_price)
    prob = model.predict_proba(customer_features)[0][1]
    if prob < 0.5:
        return base_price * 0.95
    return base_price

# Connect to the database to get the latest competitor prices
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anandsree025@',
    database='pricing_db'
)
cursor = conn.cursor()

# Read the mock store CSV
store = pd.read_csv('data/mock_store.csv')

# Update prices for each product
updated_prices = []
for _, row in store.iterrows():
    product_id = row['product_id']
    
    # Get the latest competitor price for this product
    cursor.execute("SELECT price FROM competitor_prices WHERE product_id = %s ORDER BY timestamp DESC LIMIT 1", (product_id,))
    result = cursor.fetchone()
    comp_price = result[0] if result else row['initial_price']  # Fallback to initial price if no competitor price
    
    # Apply dynamic pricing
    customer_features = pd.DataFrame({
        'price_offered': [row['initial_price']],
        'competitor_price': [comp_price],
        'time_spent': [120]  # Use a default value for time_spent
    })
    new_price = dynamic_price(comp_price, customer_features)
    
    updated_prices.append(new_price)

# Close the database connection
conn.close()

# Add the updated prices to the DataFrame
store['updated_price'] = updated_prices

# Save the updated store catalog
store.to_csv('data/mock_store_updated.csv', index=False)
print("Updated Mock Store Prices:")
print(store[['product_id', 'product_name', 'initial_price', 'updated_price']])