import pandas as pd

def transform():
    df=pd.read_csv("/home/nineleaps/airflow/dags/extracted.csv")
    df['name']=df['name'].fillna('Unknown')
    df['host_name'] = df['host_name'].fillna('Unknown')
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
    df['reviews_per_month'].fillna(0, inplace=True)
    df = df.drop_duplicates()
    df = df[df['price'] < 1000]