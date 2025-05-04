import pandas as pd
import matplotlib.pyplot as plt

# Read the updated mock store CSV
store = pd.read_csv('data/mock_store_updated.csv')

# Plot initial vs updated prices
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(store))

plt.bar(index, store['initial_price'], bar_width, label='Initial Price', color='skyblue')
plt.bar([i + bar_width for i in index], store['updated_price'], bar_width, label='Updated Price', color='lightcoral')

plt.xlabel('Products')
plt.ylabel('Price ($)')
plt.title('Initial vs Updated Prices in Mock Store')
plt.xticks([i + bar_width/2 for i in index], store['product_name'], rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig('plots/price_comparison.png')