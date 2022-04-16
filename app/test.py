from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch('localhost:9200')
index = 'postings'
body = {
    "size": 1000,
    "query": {
        "match_all": {}
    }
}

res = es.search(index=index, body=body)

print(len(res['hits']['hits']))