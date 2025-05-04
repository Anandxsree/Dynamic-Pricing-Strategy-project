Dynamic Pricing Strategy Presentation
Slide 1: Introduction

Project Title: Dynamic Pricing Strategy Analysis Using Competitor Simulation & Consumer Behavior
Objective: Develop a dynamic pricing model to optimize prices for an online store, balancing competitiveness and revenue.
Duration: 9 days (May 04, 2025, to May 12, 2025)

Slide 2: Project Phases

Day 1-2: Data Gathering - Scraped competitor prices, generated consumer behavior data, stored in pricing_db.
Day 3-4: Develop Pricing Model - Built a consumer behavior model (consumer_model.py) and dynamic pricing logic (dynamic_pricing.py).
Day 5: Test Pricing Model - Tested the model with competitor prices (test_pricing.py), analyzed results (check_prices.sql).
Day 6: Integrate with Mock Store - Applied dynamic pricing to a mock store (update_store_prices.py).
Day 7: Visualize and Analyze - Visualized price changes (visualize_results.py), analyzed revenue impact.
Day 8: Final Report - Summarized findings in dynamic_pricing_report.md.

Slide 3: Methodology

Data:
Competitor prices from competitor_prices table.
Consumer behavior data (synthetic) in consumer_behavior table.


Model:
Logistic Regression to predict purchase probability (consumer_model.pkl).
Demand-based pricing combined with consumer behavior insights.


Application:
Updated prices in mock_store.csv to mock_store_updated.csv.



Slide 4: Results

Price Changes (from mock_store_updated.csv):
Wireless Earbuds: $50.00 → $47.50
Laptop XYZ: $1000.00 → $950.00


Visualization:
Bar chart (price_comparison.png) showing initial vs updated prices.


Revenue Impact (from dynamic_pricing_report.md):
Estimated 4.5% revenue increase (e.g., Wireless Earbuds revenue: $5000 → $5225).



Slide 5: Conclusion

Success: Dynamic pricing balanced competitiveness and revenue, achieving a 4.5% revenue increase in the mock store.
Challenges Overcome:
Compatibility issues with Python 3.13 and numpy (resolved by using Python 3.12).
Empty database tables (resolved by repopulating data).


Future Improvements:
Real-time price updates.
Add features like seasonality and customer demographics.



Slide 6: Demo

Scripts: Show key scripts (consumer_model.py, dynamic_pricing.py, update_store_prices.py).
Output: Display price_comparison.png and mock_store_updated.csv.
Report: Highlight key findings from dynamic_pricing_report.md.

Slide 7: Next Steps

Deploy the model in a real online store with continuous monitoring.
Automate competitor price scraping for real-time updates.
Share the project on GitHub for portfolio visibility.

Slide 8: Q&A

Open for questions and feedback.


