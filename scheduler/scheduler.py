from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

sched = BlockingScheduler()
MONGO_HOST = 'mongo'
MONGO_PORT = '27017'
MONGO_DB = 'job'
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
ES_URL = 'elasticsearch:9200'
ES_INDEX = 'postings'
ES_DOC_TYPE = 'posting'
INDEX_SETTINGS = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1,
        "analysis": {
            "analyzer": {
            "korean_analyzer": {
                "tokenizer": "nori_tokenizer"
                }
            }
        }
    }
}

@sched.scheduled_job('interval', minutes=1, id='test_01')
def mongo2es_sync():
    myclient = MongoClient(MONGO_URI)
    mydb = myclient[MONGO_DB]
    collections = mydb.list_collection_names()
    postings = []
    
    for col_name in collections:
        col = mydb[col_name]
        docs = col.find()
        for doc in docs:
            doc['id'] = str(doc['_id'])
            del(doc['_id'])
            postings.append(doc)
    
    es_client = Elasticsearch(ES_URL, timeout=60*1)
    
    if es_client.indices.exists(index=ES_INDEX):
        es_client.indices.delete(index=ES_INDEX)

    es_client.indices.create(index=ES_INDEX, body=INDEX_SETTINGS)
    
    postings_bulk = []
    for posting in postings:
        doc = {
            '_index': ES_INDEX,
            '_type': ES_DOC_TYPE,
            '_id': posting['id'],
            '_source': posting
        }
        postings_bulk.append(doc)
        
    helpers.bulk(es_client, postings_bulk)
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, Complete mongodb data transfer into elasticsearch')

print('Scheduler Start!')
sched.start()