Dynamic Pricing Strategy Analysis
Overview
This project develops a dynamic pricing strategy for an online store using competitor price simulation and consumer behavior modeling. The goal is to optimize prices to maximize revenue while remaining competitive.
Project Structure

scripts/: Python scripts for data generation, model training, pricing, and visualization.
data/: CSV files for consumer data, mock store catalog, and test results.
plots/: Visualizations (e.g., price comparison chart).
reports/: Final report and presentation files.
requirements.txt: List of Python dependencies.

Setup

Clone the repository:git clone https://github.com/Anandxsree/Dynamic-Pricing-Strategy-project.git
cd Dynamic-Pricing-Strategy-project


Create a virtual environment and install dependencies:python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt


Set up a MySQL database (pricing_db) and update credentials in scripts if needed.
Run the scripts in order:python scripts/generate_consumer_data.py
python scripts/consumer_model.py
python scripts/dynamic_pricing.py
python scripts/test_pricing.py
python scripts/update_store_prices.py
python scripts/visualize_results.py



Results

Dynamic Pricing: Adjusted prices in a mock store, achieving a 4.5% estimated revenue increase.
Visualization: Bar chart (plots/price_comparison.png) comparing initial and updated prices.
Report: Detailed analysis in reports/dynamic_pricing_report.md.

Future Work

Deploy in a real online store with real-time updates.
Add features like seasonality and customer demographics.

Author

Anand (aspiring data analyst, fresher with experience in Python, SQL, and projects like Blinkit Grocery Data Analysis).


