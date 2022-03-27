from pymongo import MongoClient
from modules.config import Config

def mongo_load(**context):
    myclient = MongoClient(Config.MONGO_URI)
    mydb = myclient[Config.MONGO_DB]
    collection_name = context['params']['collection']
    mycollection = mydb[collection_name]

    collist = mydb.list_collection_names()

    if collection_name in collist:
        mycollection.drop()
        mycollection = mydb[collection_name]

    job_postings = context['ti'].xcom_pull(task_ids='job_posting_transform')
    # data = [posting.get_dict_posting() for posting in job_postings]
    mycollection.insert_many(job_postings)