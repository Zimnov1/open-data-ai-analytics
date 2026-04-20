import pandas as pd
import os
from sqlalchemy import create_engine

def load_data_from_db():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    return pd.read_sql("SELECT * FROM incomes", engine)

def data_research(df):
    top_5 = df.sort_values("IndicatorValue", ascending=False).head(5)
    min_value = df["IndicatorValue"].min()
    max_value = df["IndicatorValue"].max()
    ratio = max_value / min_value if min_value != 0 else None
    return top_5, min_value, max_value, ratio

if __name__ == "__main__":
    os.makedirs("artifacts/data_research", exist_ok=True)
    try:
        df = load_data_from_db()
        
        top5, min_val, max_val, ratio = data_research(df)
        
        top5.to_csv("artifacts/data_research/top5.csv", index=False)
        
        with open("artifacts/data_research/run.log", "w") as f:
            f.write(f"Top 5:\n{top5}\nMin: {min_val}, Max: {max_val}, Ratio: {ratio}\n")
        print("Data research completed.")
    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        with open("artifacts/data_research/run.log", "w") as f:
            f.write(error_msg + "\n")
        print(error_msg)