import pandas as pd
import numpy as np
import mysql.connector
from datetime import datetime

np.random.seed(42)
data = pd.DataFrame({
    'customer_id': [f'C{i}' for i in range(50)],
    'product_id': np.random.choice(['B08J5W8J9F', 'LAPTOP_ABC'], 50),
    'price_offered': np.random.uniform(40, 70, 50),
    'competitor_price': np.random.uniform(45, 75, 50),
    'time_spent': np.random.uniform(10, 300, 50).astype(int),
    'purchase': np.random.choice([0, 1], 50, p=[0.4, 0.6]),
    'timestamp': [datetime.now() for _ in range(50)]
})

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anandsree025@',
    database='pricing_db'
)
cursor = conn.cursor()

for _, row in data.iterrows():
    cursor.execute(
        "INSERT INTO consumer_behavior (customer_id, product_id, price_offered, competitor_price, time_spent, purchase, timestamp) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row['customer_id'], row['product_id'], row['price_offered'], row['competitor_price'],
         row['time_spent'], row['purchase'], row['timestamp'])
    )
conn.commit()
conn.close()
data.to_csv('data/consumer_data.csv', index=False)
print("Consumer data saved")