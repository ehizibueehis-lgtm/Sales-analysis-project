# Sales Data Analysis & Business Insights System

## Project Objective
This project analyzes a dataset of approximately 5,000 historical sales records to evaluate business performance, identify key revenue drivers, and provide actionable recommendations to management. The project includes data cleaning, exploratory data analysis (EDA), data visualization, and an Object-Oriented Python pipeline for processing future data.

## Dataset
The dataset contains 5,200 raw sales records featuring transaction details such as product name, quantity, price, regional distribution, payment method, and order status. After cleaning, the final dataset resulted in 4,480 valid records.

## Technologies Used
* **Python:** Core programming language
* **Pandas:** Data manipulation, cleaning, and aggregation
* **Matplotlib & Seaborn:** Data visualization
* **Jupyter Notebook:** Interactive data exploration and documentation
* **Git/GitHub:** Version control

## Analysis Performed
1. **Data Cleaning:** Removed duplicates, handled missing values, standardized categorical text, and converted data types.
2. **Feature Engineering:** Derived a new `total_sales` metric for revenue analysis.
3. **Exploratory Data Analysis:** Grouped and aggregated data to analyze regional performance, product popularity, and payment preferences.
4. **OOP Automation:** Built a reusable `SalesAnalyzer` class to automate the cleaning and summarization of future datasets.

## Major Findings
* **Q4 Seasonality:** October 2025 generated the highest monthly revenue ($2,828,990), indicating a massive Q4 demand spike.
* **Volume vs. Revenue:** Groundnut Oil drives the highest gross revenue, while everyday essentials like Water and Coffee drive the highest sheer transaction volume.
* **Digital Payment Dominance:** Direct bank transfers accounted for over $12 million in revenue, heavily outperforming cash and POS combined.

## Project Structure
```text
sales-analysis-project/
│
├── data/
│   ├── sales_5000.csv (Raw)
│   └── cleaned_sales_data.csv (Processed)
├── charts/
│   ├── monthly_sales_trend.png
│   ├── top_products_revenue.png
│   ├── revenue_by_payment.png
│   ├── order_status_distribution.png
│   └── top_products_quantity.png
│
├── sales-analysis-project.ipynb
├── sales_analyzer.py
├── sales_analysis_report.pdf
├── README.md
├── requirements.txt
└── .gitignore