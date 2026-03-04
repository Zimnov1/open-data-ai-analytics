import pandas as pd
import os

def data_research(df):
    top_5 = df.sort_values("IndicatorValue", ascending=False).head(5)
    min_value = df["IndicatorValue"].min()
    max_value = df["IndicatorValue"].max()
    ratio = max_value / min_value if min_value != 0 else None
    return top_5, min_value, max_value, ratio

if __name__ == "__main__":
    os.makedirs("artifacts/data_research", exist_ok=True)
    try:
        df = pd.read_excel("../data/raw/dohodi_vsi.xls")
        top5, min_val, max_val, ratio = data_research(df)
        top5.to_csv("artifacts/data_research/top5.csv", index=False)
        with open("artifacts/data_research/run.log", "w") as f:
            f.write(f"Top 5:\n{top5}\nMin: {min_val}, Max: {max_val}, Ratio: {ratio}\n")
        print("Data research completed.")
    except FileNotFoundError:
        with open("artifacts/data_research/run.log", "w") as f:
            f.write("ERROR: File not found.\n")
        print("ERROR: File not found.")