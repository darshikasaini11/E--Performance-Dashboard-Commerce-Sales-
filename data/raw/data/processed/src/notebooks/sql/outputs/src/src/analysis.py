import pandas as pd

df = pd.read_csv("../data/processed/ecommerce_cleaned.csv")

# Top categories
print(df.groupby('product_category_name')['revenue'].sum().sort_values(ascending=False).head(10))

# Monthly trend
df['month'] = pd.to_datetime(df['order_purchase_timestamp']).dt.to_period('M')
print(df.groupby('month')['revenue'].sum())
