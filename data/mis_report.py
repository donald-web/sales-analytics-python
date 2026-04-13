import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_data.csv")

# Total sales
total_sales = df["total_sales"].sum()
print("Total Sales:", total_sales)

# Sales by category
category_sales = df.groupby("category")["total_sales"].sum()

# Plot graph
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("outputs/graphs/sales_by_category.png")
plt.show()