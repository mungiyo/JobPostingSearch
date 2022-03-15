from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta

from modules.job_posting import kakao_job_posting_scraping

with DAG(
    dag_id='kakao_job_posting_scraping',
    description='카카오 채용 공고를 스크래핑하는 DAG',
    schedule_interval='0 0 3 ? * *'
) as dag:
    pass
    # Task1, 채용 공고 스크래핑
    t1 = PythonOperator(
        task_id='job_posting_scraping',
        python_callable=kakao_job_posting_scraping,
        owner='mungiyo',
        retries=3,
        retry_delay=timedelta(minutes=5)
    )

    # Task2, t1의 결과를 Kafka Cluster로 Push.