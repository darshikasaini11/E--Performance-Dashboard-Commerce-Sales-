import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("../data/processed/ecommerce_cleaned.csv")

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.to_period('M')

monthly = df.groupby('month')['revenue'].sum().reset_index()
monthly['month'] = monthly['month'].astype(str)

monthly['lag1'] = monthly['revenue'].shift(1)
monthly['lag2'] = monthly['revenue'].shift(2)

monthly = monthly.dropna()

X = monthly[['lag1', 'lag2']]
y = monthly['revenue']

model = RandomForestRegressor()
model.fit(X, y)

print("Model trained successfully!")
