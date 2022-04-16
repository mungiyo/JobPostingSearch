from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    es = Elasticsearch('localhost:9200')
    index = 'postings'
    body = {
        "size": 1000,
        "query": {
            "match_all": {}
        }
    }
    
    res = es.search(index=index, body=body)
    
    sources = [source['_source'] for source in res['hits']['hits']]
    
    return render_template('index.html', sources=sources)

if __name__ == '__main__':
    app.run(debug=True)