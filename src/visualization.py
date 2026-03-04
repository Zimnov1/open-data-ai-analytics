import pandas as pd
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    os.makedirs("artifacts/visualization", exist_ok=True)
    try:
        df = pd.read_excel("data/raw/dohodi_vsi.xls")
        df_grouped = df.groupby('Community')['IndicatorValue'].sum().sort_values(ascending=False)
        top10 = df_grouped.head(10)

        plt.figure(figsize=(10,6))
        top10.plot(kind='bar')
        plt.title('Top 10 communities by income')
        plt.ylabel('Amount of income (thousand UAH)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig("artifacts/visualization/top10_income.png")
        plt.close()

        with open("artifacts/visualization/run.log", "w") as f:
            f.write("Visualization generated successfully.\n")
        print("Visualization completed.")
    except FileNotFoundError:
        with open("artifacts/visualization/run.log", "w") as f:
            f.write("ERROR: File not found.\n")
        print("ERROR: File not found.")