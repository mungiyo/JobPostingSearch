from konlpy.tag import Okt
from pymongo import MongoClient
from config import Config

def text_transform(**context):
    okt = Okt()
    job_postings = context['ti'].xcom_pull(task_ids='job_posting_scraping')
    
    myclient = MongoClient(Config.MONGO_URI)
    mydb = myclient[Config.MONGO_DB]
    mycol = mydb[job_postings[0]['company']]
    docs = mycol.find()
    url_list = [doc['url'] for doc in docs]
    for posting in job_postings:
        if posting['url'] in url_list:
            i = url_list.index(posting['url'])
            posting['scraped_time'] = docs[i]['scraped_time']
        posting['contents'] = posting['contents'].replace('\n', ' ')
    
    return job_postings