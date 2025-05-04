Dynamic Pricing Strategy Analysis Report
Project Overview
This project aimed to develop a dynamic pricing strategy using competitor price simulation and consumer behavior modeling. The goal was to optimize prices for a mock online store to maximize revenue while remaining competitive.
Methodology

Data Collection: Gathered competitor prices and consumer behavior data (e.g., time spent, purchase decisions) using web scraping and synthetic data generation.
Model Development: Built a consumer behavior model using logistic regression to predict purchase probability based on price offered, competitor price, and time spent.
Dynamic Pricing: Combined a demand-based pricing model with the consumer behavior model to adjust prices dynamically.
Mock Store Integration: Applied the dynamic pricing model to a mock store catalog (mock_store.csv) and updated prices based on the latest competitor data.

Results

Price Changes: The updated prices for the mock store products are as follows (from mock_store_updated.csv):
Wireless Earbuds: Initial $50.00, Updated $47.50
Laptop XYZ: Initial $1000.00, Updated $950.00


Visualization: A bar chart (plots/price_comparison.png) was generated to compare initial and updated prices, showing a consistent price reduction to improve purchase probability.
Revenue Impact: Assuming a 10% demand increase for every 5% price decrease:
Wireless Earbuds: Demand increased from 100 to 110 units, revenue from $5000 to $5225.
Laptop XYZ: Demand increased from 10 to 11 units, revenue from $10,000 to $10,450.
Total revenue increased by approximately 4.5%.



Conclusion
The dynamic pricing strategy successfully adjusted prices to balance competitiveness and revenue. The consumer behavior model effectively identified when price reductions were needed to boost purchase probability, leading to an estimated 4.5% revenue increase in the mock store. Future improvements could include real-time price updates and incorporating additional factors like seasonality.
Recommendations

Implement the dynamic pricing model in a real online store with continuous monitoring.
Enhance the model by adding more features (e.g., customer demographics, seasonal trends).
Automate competitor price scraping for real-time updates.

