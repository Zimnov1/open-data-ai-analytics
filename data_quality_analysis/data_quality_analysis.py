import pandas as pd
import os
from sqlalchemy import create_engine

def load_data_from_db():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    return pd.read_sql("SELECT * FROM incomes", engine), engine

def data_quality(df):
    na_counts = df.isna().sum().to_frame(name='null_count').reset_index()
    stats = df.describe()
    return na_counts, stats

if __name__ == "__main__":
    os.makedirs("artifacts/data_quality_analysis", exist_ok=True)
    try:
        df, engine = load_data_from_db()
        
        na_counts, stats = data_quality(df)
        
        na_counts.to_sql("quality_metrics", engine, if_exists='replace', index=False)
        
        stats.to_csv("artifacts/data_quality_analysis/stats.csv")
        
        with open("artifacts/data_quality_analysis/run.log", "w") as f:
            f.write("Data Quality Analysis Completed and saved to DB.\n")
            f.write(f"NA counts saved to table 'quality_metrics'\n")
        print("Data quality analysis completed.")
    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        with open("artifacts/data_quality_analysis/run.log", "w") as f:
            f.write(error_msg + "\n")
        print(error_msg)