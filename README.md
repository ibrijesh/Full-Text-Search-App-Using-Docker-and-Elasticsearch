# FULL-TEXT SEARCH APP USING DOCKER AND ELASTICSEARCH

### Aim of this  project was to demonstrate  how fast  is  searching text  using elasticsearch as database.

Elasticsearch uses a data structure called an inverted index, which is designed to allow very fast full-text searches. An inverted index lists every unique word that appears in any document and identifies all of the documents each word occurs in.

During the indexing process, Elasticsearch stores documents and builds an inverted index to make the document data searchable in near real-time. Indexing is initiated with the index API, through which you can add or update a JSON document in a specific index.

<br>

## You can view live demo of project  at  
``` 
https://search.ibrijesh.me
```

<br>
<br>


![stack](https://user-images.githubusercontent.com/41025295/126439945-7e4a5c3b-776e-4c1b-adec-81237f9b630b.gif)

<br>
<br>

# Architecture
<br>

![stackoverflow](https://user-images.githubusercontent.com/41025295/126470394-bfe16bf1-3a04-4015-bc89-69621bcf32c3.png)


<br>
<br>


# If you want to  run or play with this project on your system , follow the below steps.

## Requirements

- git
- docker
- docker-compose

### Steps 1
```
git clone https://github.com/ibrijesh/stackoverflow-questions-search-using-elasticsearch
```

### Step 2
- open the folder stackoverflow-questions-search-using-elasticsearch 
``` 
cd stackoverflow-questions-search-using-elasticsearch
```

### Step 3
- Run the commad
```
docker-compose up -d --build  
```  
- wait for few minutes

### Step 4
- go to your favourite browser and  type
```
http://localhost:8080 
```
<br>
<br>

## ❌ How to Avoid  Common Error  
- Make sure that  no other  process is already running on ports 8080 , 8000 ,5000 ,9200 ,9300


