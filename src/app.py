import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce ML Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/processed/predictions_for_powerbi.csv")

st.title("📊 E-Commerce Sales ML Dashboard")

# ---------------------------
# DATA PREVIEW
# ---------------------------
st.subheader("📁 Dataset Preview")
st.dataframe(df.head())

# ---------------------------
# METRICS
# ---------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Actual Revenue", round(df["actual_revenue"].mean(), 2))
col2.metric("Avg Predicted Revenue", round(df["predicted_revenue"].mean(), 2))
col3.metric("Avg Error", round((df["actual_revenue"] - df["predicted_revenue"]).mean(), 2))

# ---------------------------
# CHART: ACTUAL VS PREDICTED
# ---------------------------
st.subheader("📈 Actual vs Predicted Revenue")

chart_data = df[["actual_revenue", "predicted_revenue"]]
st.line_chart(chart_data)

# ---------------------------
# ERROR ANALYSIS
# ---------------------------
st.subheader("📉 Error Distribution")

df["error"] = df["actual_revenue"] - df["predicted_revenue"]
st.bar_chart(df["error"])

# ---------------------------
# SIMPLE PREDICTION DEMO
# ---------------------------
st.subheader("🔮 Try Prediction")

price = st.number_input("Price", value=100)
freight = st.number_input("Freight Value", value=10)

if st.button("Predict Revenue"):
    prediction = price + freight  # simple logic fallback
    st.success(f"Predicted Revenue: {prediction}")