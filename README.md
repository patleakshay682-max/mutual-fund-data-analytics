Mutual Fund Data Analytics & Power BI Dashboard

📊 Project Overview
This project analyzes mutual fund data using Python, SQL, and Microsoft Power BI. The dashboard provides interactive insights into mutual fund industry trends, fund performance, investor transactions, SIP inflows, and market trends.

🎯 Project Objective
The main objectives of this project are:

Analyze mutual fund industry AUM and folio trends
Compare mutual fund performance and risk
Analyze investor transactions and investment behavior
Study monthly SIP inflows
Analyze category-wise inflows
Compare SIP trends with market benchmark performance
Build an interactive Power BI dashboard
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
SQL
SQLite
Microsoft Power BI
Jupyter Notebook
📑 Dashboard Pages
1. Industry Overview
Total AUM
SIP Inflows
Total Folios
Total Schemes
Industry AUM Trend
AUM by Fund House
Monthly SIP Inflow Trend
Industry Folios Trend
2. Fund Performance
Return vs Risk Analysis
Performance Scorecard
NAV vs Benchmark Trend
Fund House, Category, and Plan filters
3. Investor Analysis
Total Transactions
Total Investment
Total Redemption
Average Transaction Amount
Transaction Amount by State
Transaction Type Split
Age Group vs Average SIP Amount
Monthly Transaction Volume
4. SIP & Market Trends
SIP Inflow vs Nifty 50 Trend
Category Inflow Heatmap
Top 5 Categories by Net Inflow — FY25
📁 Project Structure
mutual-fund-data-analytics/
│
├── README.md
├── data_ingestion.ipynb
├── data_ingestion.py
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── database/
│   └── bluestock_mf.db
│
├── dashboard/
│   ├── Mutual_Fund_Dashboard.pbix
│   └── Mutual_Fund_Dashboard.pdf
│
└── screenshots/
    ├── Page1_Industry_Overview.png
    ├── Page2_Fund_Performance.png
    ├── Page3_Investor_Analysis.png
    └── Page4_SIP_Market_Trends.png
