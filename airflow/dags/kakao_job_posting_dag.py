from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from modules.job_posting_scraper import kakao_job_posting_scraping

with DAG(
    dag_id='kakao_job_posting_scraping',
    description='카카오 채용 공고를 스크래핑하는 DAG',
    schedule_interval='0 0 3 ? * *'
) as dag:
    pass
    # t1, 현재 DB의 채용 공고 리스트 리턴

    # t2, 채용 공고 스크래핑 결과 리턴

    # t3, 스크래핑 결과를 받아서 kafka broker로 load