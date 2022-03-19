from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

from modules.job_posting_crawler import kakao_job_posting_crawling

with DAG(
    dag_id='kakao_job_posting_scraping',
    description='카카오 채용 공고를 스크래핑하는 DAG',
    schedule_interval='0 0 3 ? * *'
) as dag:
    # Task1, 채용 공고 크롤링
    t1 = PythonOperator(
        task_id='job_posting_crawling',
        python_callable=kakao_job_posting_crawling,
        owner='mungiyo',
        retries=3,
        retry_delay=timedelta(minutes=5)
    )

    # Task2, t1의 결과를 transform
    t2 = PythonOperator()

    # Task3, t2의 결과를 mongodb로 load
    t3 = PythonOperator()

    t1 >> t2 >> t3