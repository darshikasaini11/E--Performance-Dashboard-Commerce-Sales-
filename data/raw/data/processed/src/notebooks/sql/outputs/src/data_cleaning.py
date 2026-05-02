import pandas as pd

orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")
products = pd.read_csv("data/raw/products.csv")
customers = pd.read_csv("data/raw/customers.csv")

df = orders.merge(order_items, on="order_id") \
           .merge(products, on="product_id") \
           .merge(customers, on="customer_id")

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['revenue'] = df['price'] + df['freight_value']

df.to_csv("data/processed/ecommerce_cleaned.csv", index=False)

print("Data cleaned successfully!")
