import pandas as pd
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine

def load_data_from_db():
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    return pd.read_sql("SELECT * FROM incomes", engine)

if __name__ == "__main__":
    os.makedirs("artifacts/visualization", exist_ok=True)
    try:
        df = load_data_from_db()
        
        df_grouped = df.groupby('Community')['IndicatorValue'].sum().sort_values(ascending=False)
        top10 = df_grouped.head(10)

        plt.figure(figsize=(10,6))
        top10.plot(kind='bar', color='skyblue')
        plt.title('Top 10 communities by income (from DB)')
        plt.ylabel('Amount of income (thousand UAH)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        plt.savefig("artifacts/visualization/top10_income.png")
        plt.close()

        with open("artifacts/visualization/run.log", "w") as f:
            f.write("Visualization generated from DB data successfully.\n")
        print("Visualization completed.")
    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        with open("artifacts/visualization/run.log", "w") as f:
            f.write(error_msg + "\n")
        print(error_msg)