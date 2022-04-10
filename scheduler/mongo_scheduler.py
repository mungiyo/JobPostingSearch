from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

sched = BlockingScheduler()
MONGO_HOST = 'localhost'
MONGO_PORT = '27020'
MONGO_DB = 'job'
MONGO_COLLECTION = 'postings'
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?replicaSet=replication&readPreference=primary&directConnection=true&ssl=false"

@sched.scheduled_job('interval', seconds=30, id='test_01')
def mongo_sync():
    myclient = MongoClient(MONGO_URI)
    mydb = myclient[MONGO_DB]
    mydb[MONGO_COLLECTION].drop()

    collections = mydb.list_collection_names()
    total_data = []
    for col_name in collections:
        col = mydb[col_name]
        docs = col.find()
        for doc in docs: total_data.append(doc)
        
    posting_col = mydb[MONGO_COLLECTION]
    posting_col.insert_many(total_data)

    end_time = datetime.now()
    print(f'{end_time} mongodb collection synchronizing.')

print('Scheduler Start!')
sched.start()