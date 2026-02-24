import pandas as pd

def data_research(df):
    top_5 = df.sort_values("IndicatorValue", ascending=False).head(5)
    print(top_5[["Community", "IndicatorValue"]])
    min_value = df["IndicatorValue"].min()
    max_value = df["IndicatorValue"].max()
    print("Min:", min_value, "Max:", max_value, "Ratio:", max_value/min_value)

if __name__ == "__main__":
    df = pd.read_excel("../data/raw/dohodi_vsi.xls")
    data_research(df)