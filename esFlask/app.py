import json
import time
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
# import tensorflow as tf
# import tensorflow_hub as hub
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


# # Search by Vec Similarity
# def sentenceSimilaritybyNN(es, sent,offset):
#     query_vector = tf.make_ndarray(tf.make_tensor_proto(embed([sent]))).tolist()[0]
#     b = {
#            "from":offset,
#            "size":10,
#            "_source":{
#                      "excludes":["body_content","title_vector"]
#             },
#            "query" : {
#                 "script_score" : {
#                     "query" : {
#                         "match_all": {}
#                     },
#                     "script" : {
#                         "source": "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
#                         "params": {"query_vector": query_vector}
#                     }
#                 }
#              }
#         }



#     #print(json.dumps(b,indent=4))
#     res= es.search(index='questions-index',body=b)
    
#     return res;


app = Flask(__name__)
es = connect2ES();
#embed = hub.load("./USE4")


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
    # res_semantic = sentenceSimilaritybyNN( es, q, offset)

    ret = ""
    for hit in res_kw['hits']['hits']:
        ret += (" KW: " + str( hit['_score']) + "\t" + hit['_source']['title'] +"\n" )

    # for hit in res_semantic['hits']['hits']:
    #     ret += (" Semantic: " +str(hit['_score']) + "\t" + hit['_source']['title'] +"\n")
    return res_kw
    


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    




#             "_source":{
             #        "excludes":["title_vector"]
            #},
