import requests
import json
import os
from elasticsearch import Elasticsearch

directory = './emails/'
res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

i = 1

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(directory+filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket',
        id=i, body=json.loads(docket_content.replace('\r\n\t\0', ''), strict=False))
        i = i + 1