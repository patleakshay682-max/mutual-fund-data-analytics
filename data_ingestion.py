from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows (1).csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

datasets = {}

print("MUTUAL FUND DATA INGESTION")
print("=" * 60)

for filename in files:
    file_path = RAW_DIR / filename

    if file_path.exists():
        df = pd.read_csv(file_path)
        datasets[filename] = df

        print("\nFile:", filename)
        print("Shape:", df.shape)
        print("Missing values:", df.isnull().sum().sum())
        print("Duplicate rows:", df.duplicated().sum())
    else:
        print("\nFILE NOT FOUND:", filename)

print("\n" + "=" * 60)
print("DATA INGESTION COMPLETE")
print("Datasets loaded:", len(datasets))
