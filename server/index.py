import json
import time
import sys
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import csv
from flask import Flask
from flask_cors import CORS
from flask import request


# connect to ES on localhost on port 9200

# host= localhost or IP address of machine  when not connecting to docker container 

es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
if es.ping():
	print('Connected to ES!')
else:
	print('Could not connect!')
	sys.exit()

print("*********************************************************************************");


# index in ES = DB in an RDBMS
# Read each question and index into an index called questions
# Indexing only titles for this example to improve speed. In practice, its good to index CONCATENATE(title+body)
# Define the index


#Refer: https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html
# Mapping: Structure of the index
# Property/Field: name and type  

b = {"mappings": {
  	"properties": {
		    "id":{
				"type":"text"
			},
			"title": {
      			"type": "text"
    		},
			"body": {
				"type":"text"
			},
			"tag": {
				"type":[]
			}
	}
     }
   }



ret = es.indices.create(index='questions-index', ignore=400, body=b) #400 caused by IndexAlreadyExistsException, 
print(json.dumps(ret,indent=4))

# TRY this in browser: http://localhost:9200/questions-index

print("*********************************************************************************");

#sys.exit();




# CONSTANTS
NUM_QUESTIONS_INDEXED = 200

# Col-Names: Id,OwnerUserId,CreationDate,ClosedDate,Score,Title,Body
cnt=0

with open('./QT.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',' )
	next(readCSV, None)  # skip the headers 
	for row in readCSV:
		#print(row[0], row[5])
		doc_id = row[1];
		title = row[3];
		body_content = row[4];
		tag=row[5];
		#vec = tf.make_ndarray(tf.make_tensor_proto(embed([title]))).tolist()[0]		
		
		b = {
			"id":doc_id,
			"title":title,
			"body":body_content,
			"tag":tag
			}	

		#print(json.dumps(tmp,indent=4))		
		res = es.index(index="questions-index", id=doc_id, body=b)
		#print(cnt)
		# keep count of # rows processed
		cnt += 1
		if cnt%100==0:
			print(cnt)
		
		if cnt == NUM_QUESTIONS_INDEXED:
			break;

	print("Completed indexing....")

	print("*********************************************************************************");
	




