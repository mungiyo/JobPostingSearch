from flask import Flask, render_template
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

@app.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')

@app.route('/password', methods=['GET'])
def password():
    return render_template('auth/password.html')

@app.route('/tables', methods=['GET'])
def tables():
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
    
    return render_template('addons/tables.html', sources=sources)

@app.route('/charts', methods=['GET'])
def charts():
    return render_template('addons/charts.html')

if __name__ == '__main__':
    app.run(debug=True)