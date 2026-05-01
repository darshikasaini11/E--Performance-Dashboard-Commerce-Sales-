import pandas as pd

# Load raw data
orders = pd.read_csv("../data/raw/orders.csv")
order_items = pd.read_csv("../data/raw/order_items.csv")
products = pd.read_csv("../data/raw/products.csv")
customers = pd.read_csv("../data/raw/customers.csv")

# Merge datasets
df = orders.merge(order_items, on="order_id") \
           .merge(products, on="product_id") \
           .merge(customers, on="customer_id")

# Convert date
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Feature engineering
df['revenue'] = df['price'] + df['freight_value']

# Save cleaned data
df.to_csv("../data/processed/ecommerce_cleaned.csv", index=False)

print("Data cleaned successfully!")
