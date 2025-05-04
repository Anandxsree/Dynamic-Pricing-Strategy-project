from sklearn.linear_model import LogisticRegression
import pandas as pd
import mysql.connector
import joblib

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anandsree025@',
    database='pricing_db'
)
data = pd.read_sql("SELECT price_offered, competitor_price, time_spent, purchase FROM consumer_behavior", conn)
conn.close()

X = data[['price_offered', 'competitor_price', 'time_spent']]
y = data['purchase']
model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, 'models/consumer_model.pkl')

new_data = pd.DataFrame({
    'price_offered': [50],
    'competitor_price': [55],
    'time_spent': [120]
})
prob = model.predict_proba(new_data)[0][1]
print(f"Purchase Probability: {prob:.2%}")