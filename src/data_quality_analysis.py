import pandas as pd
import os

def data_quality(df):
    info = df.info()
    na_counts = df.isna().sum()
    stats = df.describe()
    return info, na_counts, stats

if __name__ == "__main__":
    os.makedirs("artifacts/data_quality_analysis", exist_ok=True)
    try:
        df = pd.read_excel("../data/raw/dohodi_vsi.xls")
        info, na_counts, stats = data_quality(df)
        stats.to_csv("artifacts/data_quality_analysis/stats.csv")
        with open("artifacts/data_quality_analysis/run.log", "w") as f:
            f.write("Data Quality Analysis Completed.\n")
            f.write(f"NA counts:\n{na_counts}\n")
        print("Data quality analysis completed.")
    except FileNotFoundError:
        with open("artifacts/data_quality_analysis/run.log", "w") as f:
            f.write("ERROR: File not found.\n")
        print("ERROR: File not found.")