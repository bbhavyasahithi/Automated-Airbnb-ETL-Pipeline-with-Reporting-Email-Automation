import pandas as pd

def load():
    df=pd.read_csv("/home/nineleaps/airflow/dags/extracted.csv")
    df.to_csv("/home/nineleaps/airflow/dags/final_data.csv")