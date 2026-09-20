from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load
from scripts.email_report import send_email
from scripts.eda import eda

with DAG(
    dag_id="airbnb_etl_pipeline",
    start_date=datetime(2026, 4, 28),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)
    t4 = PythonOperator(task_id="eda", python_callable=eda)
    t5 = PythonOperator(task_id="send_email",python_callable=send_email)

    t1 >> t2 >> t3 >> t4 >> t5
