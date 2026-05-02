import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("data/processed/ecommerce_cleaned.csv")

# Drop missing values
df = df.dropna()

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

# Convert date
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Time features
df['order_month'] = df['order_purchase_timestamp'].dt.month
df['order_dayofweek'] = df['order_purchase_timestamp'].dt.dayofweek

# Freight ratio (important in e-commerce)
df['freight_ratio'] = df['freight_value'] / (df['price'] + 1)

# Encode category (simple label encoding)
df['product_category'] = df['product_category_name'].astype('category').cat.codes

# Target
df['revenue'] = df['price'] + df['freight_value']

# -----------------------------
# FEATURES & TARGET
# -----------------------------
features = [
    'price',
    'freight_value',
    'order_month',
    'order_dayofweek',
    'freight_ratio',
    'product_category'
]

X = df[features]
y = df['revenue']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model (stronger tuned version)
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)

print("🚀 Improved Model Training Completed")
print("Mean Absolute Error:", mae)

# Sample prediction
sample = pd.DataFrame([[
    100,   # price
    10,    # freight_value
    6,     # month
    2,     # weekday
    0.1,   # freight_ratio
    1      # category encoded
]], columns=features)

print("Sample Prediction:", model.predict(sample))


# Save predictions for Power BI
results = X_test.copy()
results["actual_revenue"] = y_test.values
results["predicted_revenue"] = y_pred

results.to_csv("data/processed/predictions_for_powerbi.csv", index=False)

print("📊 File saved for Power BI integration!")