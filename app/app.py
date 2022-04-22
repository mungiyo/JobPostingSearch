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
    
    return render_template('index/index.html', sources=sources)

@app.route('/postings', methods=['GET', 'POST'])
def postings():
    if request.method == 'GET':
        search_text = request.args["search"]
        es = Elasticsearch('localhost:9200')
        index = 'postings'
        if search_text == "":
            body = {
                "size": 1000,
                "query": {
                    "match_all": {}
                }
            }
        else:
            body = {
                "size": 1000,
                "query": {
                    "multi_match": {
                        "query": search_text,
                        "fields": ["title", "contents"]
                    }
                }
            }
        
        res = es.search(index=index, body=body)
        sources = [source['_source'] for source in res['hits']['hits']]
        
        return render_template('addons/tables.html', sources=sources)


if __name__ == '__main__':
    app.run(debug=True)