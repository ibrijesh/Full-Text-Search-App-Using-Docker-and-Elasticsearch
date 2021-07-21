# Stackoverflow questions searching using elasticsearch as database

This project was made to demonstrate that how fast it is to search for keyword based documents using elasticsearch.

## You can view live demo of project  at  
``` 
https://ibrijesh.centralindia.cloudapp.azure.com/ 
```

<br>
<br>


![stack](https://user-images.githubusercontent.com/41025295/126439945-7e4a5c3b-776e-4c1b-adec-81237f9b630b.gif)

<br>
<br>

# System Design of This Project

![stackoverflow](https://user-images.githubusercontent.com/41025295/126460959-2cb7ec8e-84c0-4014-aa4c-5ba5ab119f93.png)


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
- Make sure no process is already running on ports 8080 , 8000 ,5000 ,9200 ,9300


