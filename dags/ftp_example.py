from airflow import DAG
from airflow.providers.ftp.operators.ftp import FTPDownloadOperator
from airflow.providers.ftp.hooks.ftp import FTPHook
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1)
}

with DAG('ftp_example', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    
    # Define the FTP connection parameters
    ftp_conn = FTPHook(
        ftp_conn_id='ftp_default',
        host='ftp.dlptest.com',
        port=21,
        username='dlpuser',
        password='rNrKYTX9g7z3RgJRmxWuGHbeu'
    )
    
    # Use the FTP connection in the FTPDownloadOperator
    download_task = FTPDownloadOperator(
        task_id='download_file',
        ftp_conn=ftp_conn,
        local_filepath='/path/to/local/file.txt',
        remote_filepath='/path/to/remote/file.txt'
    )

    download_task
