from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    schedule_interval='@once',
)

send_email = EmailOperator(
    task_id='send_email',
    to='joavelar@microsoft.com',
    subject='Airflow Alert',
    html_content='<h3>Hello World</h3>',
    dag=dag,
)
