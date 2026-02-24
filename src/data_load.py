import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = pd.read_excel("../data/raw/dohodi_vsi.xls")
    print(df.head())