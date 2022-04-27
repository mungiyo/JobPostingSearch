from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/postings', methods=['GET'])
def postings():
    if request.method == 'GET':
        try:
            search_text = request.args["search"]
        except KeyError:
            search_text = ""
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
        res = {
            'postings_total_size': len(sources),
            'source': sources
        }
        
        return jsonify(res), 200

if __name__ == '__main__':
    app.run(debug=True)