import fireducks as fd
df = fd.read_csv('sales_data.csv')
grouped_df = df.groupby('Product')['Sales'].mean()
print(grouped_df)
