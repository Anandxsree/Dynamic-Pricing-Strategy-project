import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime

# Attempt to scrape Amazon
try:
    url = 'https://www.amazon.com/dp/B08J5W8J9F'  # Earbuds
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    product_id = 'B08J5W8J9F'

    # Try to find product name
    product_elem = soup.find('span', id='productTitle')
    product_name = product_elem.text.strip() if product_elem else 'Wireless Earbuds (Scraping Failed)'

    # Try to find price
    price_elem = soup.find('span', class_='a-price-whole')
    if price_elem:
        price = float(price_elem.text.replace('$', '').replace(',', ''))
    else:
        price = 50.00  # Fallback price if scraping fails

except Exception as e:
    print(f"Scraping failed: {e}")
    product_id = 'B08J5W8J9F'
    product_name = 'Wireless Earbuds (Scraping Failed)'
    price = 50.00  # Fallback price

# Save to database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anandsree025@',
    database='pricing_db'
)
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO competitor_prices (product_id, product_name, price, competitor, timestamp) "
    "VALUES (%s, %s, %s, %s, %s)",
    (product_id, product_name, price, 'Amazon', datetime.now())
)
conn.commit()
conn.close()
print(f"Saved: {product_name}, Price: ${price}")