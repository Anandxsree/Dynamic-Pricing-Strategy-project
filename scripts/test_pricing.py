import mysql.connector
import pandas as pd
import joblib
import numpy as np

model = joblib.load('models/consumer_model.pkl')

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

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anandsree025@',
    database='pricing_db'
)
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT price FROM competitor_prices WHERE product_id = 'B08J5W8J9F' LIMIT 3")
comp_prices = [row[0] for row in cursor.fetchall()]
conn.close()

results = []
for cp in comp_prices:
    price = dynamic_price(cp, pd.DataFrame({
        'price_offered': [50],
        'competitor_price': [cp],
        'time_spent': [120]
    }))
    results.append({'competitor_price': cp, 'dynamic_price': price})

pd.DataFrame(results).to_csv('data/test_results.csv', index=False)
print(pd.read_csv('data/test_results.csv'))