import pandas as pd

def extract():
    df=pd.read_csv("/home/nineleaps/airflow/dags/AB_NYC_2019.csv")
    df.to_csv("/home/nineleaps/airflow/dags/extracted.csv", index=False)
    print("Extract completed")