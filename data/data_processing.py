import pandas as pd

df = pd.read_csv("data/sales_data.csv")

# Create total sales column
df["total_sales"] = df["price"] * df["quantity"]

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

# Save processed data
df.to_csv("data/processed_data.csv", index=False)

print("Data Processed Successfully!")