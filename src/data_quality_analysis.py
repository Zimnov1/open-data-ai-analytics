import pandas as pd

def data_quality(df):
    print(df.info())
    print(df.isna().sum())
    print(df.describe())

if __name__ == "__main__":
    df = pd.read_excel("../data/raw/dohodi_vsi.xls")
    data_quality(df)