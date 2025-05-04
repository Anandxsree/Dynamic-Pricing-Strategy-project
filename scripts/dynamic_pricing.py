import joblib
import pandas as pd
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

customer_features = pd.DataFrame({
    'price_offered': [50],
    'competitor_price': [55],
    'time_spent': [120]
})
price = dynamic_price(55, customer_features)
print(f"Dynamic Price: ${price:.2f}")