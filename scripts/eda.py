import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda():
    df = pd.read_csv("/home/nineleaps/airflow/dags/final_data.csv")
    plt.figure()
    sns.histplot(df['price'], bins=10)
    plt.title("Price Distribution")
    plt.savefig("/home/nineleaps/airflow/dags/output/price_distribution.png")

    plt.figure()
    df['room_type'].value_counts().plot(kind='bar')
    plt.title("Room Type Distribution")
    plt.savefig("/home/nineleaps/airflow/dags/output/room_type.png")

    plt.figure()
    df.groupby('neighbourhood_group')['price'].mean().plot(kind='bar')
    plt.title("Avg Price by Area")
    plt.savefig("/home/nineleaps/airflow/dags/output/price_by_area.png")

        # -----------------------------
    # Generate KPI Summary
    # -----------------------------
    total_records = len(df)
    avg_price = round(df["price"].mean(), 2)
    max_price = df["price"].max()
    min_price = df["price"].min()

    summary = f"""
Airbnb ETL Pipeline Summary

Total Listings : {total_records}
Average Price  : {avg_price}
Maximum Price  : {max_price}
Minimum Price  : {min_price}
"""

    with open("/home/nineleaps/airflow/dags/output/summary.txt", "w") as f:
        f.write(summary)

    print("EDA completed")