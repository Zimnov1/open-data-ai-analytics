import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/raw/dohodi_vsi.xls")

df_grouped = df.groupby('Community')['IndicatorValue'].sum().sort_values(ascending=False)

top10 = df_grouped.head(10)
plt.figure(figsize=(10,6))
top10.plot(kind='bar')
plt.title('Top 10 communities by income')
plt.ylabel('Amount of income (thousand UAH)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()