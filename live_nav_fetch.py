import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"

schemes = {
    "125497": "SBI Small Cap Fund",
    "119551": "SBI Bluechip Fund - Task Code",
    "120503": "ICICI Pru Bluechip Fund - Task Code",
    "118632": "Nippon India Large Cap Fund",
    "119092": "Axis Bluechip Fund - Task Code",
    "120841": "Kotak Bluechip Fund - Task Code"
}

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        df["amfi_code"] = code
        df["scheme_name"] = data["meta"]["scheme_name"]

        output_file = RAW_DIR / f"live_nav_{code}.csv"

        df.to_csv(output_file, index=False)

        print(f"{code}: {len(df)} records saved")

    else:
        print(f"{code}: API request failed - {response.status_code}")

print("Live NAV fetching complete.")
