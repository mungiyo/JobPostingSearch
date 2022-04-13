from pymongo import MongoClient
from config import Config

def mongo_load(**context):
    myclient = MongoClient(Config.MONGO_URI)
    mydb = myclient[Config.MONGO_DB]
    collection_name = context['params']['collection']
    collist = mydb.list_collection_names()

    if collection_name in collist:
        mycollection = mydb[collection_name]
        mycollection.drop()
        
    else:
        mycollection = mydb[collection_name]

    job_postings = context['ti'].xcom_pull(task_ids='job_posting_transform')
    mycollection.insert_many(job_postings)