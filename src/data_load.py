import pandas as pd
import os

def load_data(path):
    df = pd.read_excel(path)
    return df

if __name__ == "__main__":
    os.makedirs("artifacts/data_load", exist_ok=True)
    try:
        df = load_data("data/raw/dohodi_vsi.xls")
        df.to_csv("artifacts/data_load/dataset.csv", index=False)
        with open("artifacts/data_load/run.log", "w") as f:
            f.write("Data loaded successfully.\nRows: {}\nColumns: {}".format(df.shape[0], df.shape[1]))
        print("Data loaded successfully.")
    except FileNotFoundError:
        with open("artifacts/data_load/run.log", "w") as f:
            f.write("ERROR: File not found.\n")
        print("ERROR: File not found.")