import pandas as pd

df = pd.read_csv("data/processed_data.csv")

while True:
    query = input("Ask something (type 'exit' to quit): ").lower()

    if query == "exit":
        break

    elif "total sales" in query:
        print("Total Sales:", df["total_sales"].sum())

    elif "top product" in query:
        top = df.groupby("product_name")["total_sales"].sum().idxmax()
        print("Top Product:", top)

    else:
        print("Sorry, I don't understand.")