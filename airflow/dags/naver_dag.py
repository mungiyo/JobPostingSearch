# airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# modules
from job_posting_scraper import naver_job_posting_scraping
from job_posting_transform import text_transform
from job_posting_load import mongo_load
# library
from datetime import timedelta, datetime

with DAG(
    dag_id='naver_job_posting_ETL',
    description='naver job postings scraping DAG',
    start_date=datetime(2022, 4, 13),
    schedule_interval=timedelta(hours=3)
) as dag:
    # Task1, job posting scraping
    t1 = PythonOperator(
        task_id='job_posting_scraping',
        python_callable=naver_job_posting_scraping,
        provide_context=True,
        owner='mungiyo',
        retries=3,
        retry_delay=timedelta(minutes=5)
    )

    # Task2, result of t1 transform
    t2 = PythonOperator(
        task_id='job_posting_transform',
        python_callable=text_transform,
        provide_context=True,
        owner='mungiyo',
        retries=3,
        retry_delay=timedelta(minutes=5)
    )

    # Task3, result of t2 load to mongodb
    t3 = PythonOperator(
        task_id='job_posting_load',
        python_callable=mongo_load,
        params={'collection': 'naver'},
        provide_context=True,
        owner='mungiyo',
        retries=3,
        retry_delay=timedelta(minutes=5)
    )

    t1 >> t2 >> t3