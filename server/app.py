import json
import time
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
from flask import Flask
from flask_cors import CORS
from flask import request






def connect2ES():
    # connect to ES on localhost on port 9200
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    if es.ping():
            print('Connected to ES!')
    else:
            print('Could not connect!')
            sys.exit()

    print("*********************************************************************************");
    return es

def keywordSearch(es, q,offset):
    #Search by Keywords
    b={
            "from":offset,
            "size":15,
            "query":{
                "match":{
                    "title":{
                        "query":q,
                        "fuzziness":'AUTO'
                    }
                }
            }
        }

    res= es.search(index='questions-index',body=b)

    return res



app = Flask(__name__)
es = connect2ES();



CORS(app)




@app.route('/')
@app.route('/hello')
def HelloWorld():
    return 'Hello World'
@app.route('/search',methods=['GET','POST'])
def search():
    #q = query.replace("+", " ")
    q=request.args.get('term')
    offset=request.args.get('offset')
    print('\n',q)
    print('\n',offset)
    res_kw = keywordSearch(es, q,offset)

    ret = ""
    for hit in res_kw['hits']['hits']:
        ret += (" KW: " + str( hit['_score']) + "\t" + hit['_source']['title'] +"\n" )
    return res_kw
    


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
