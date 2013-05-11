#!/usr/bin/python
# -*- coding: utf-8 -*-"
import requests, datetime
from glob import glob
from json import loads
from datetime import datetime
from pymongo import Connection

# JSON representations of threads and indexes:
# http(s)://api.4chan.org/**board**/res/**threadnumber**.json
# http(s)://api.4chan.org/**board**/**pagenumber**.json (0 is main index)

#### Get jsons:

urls = [ "http://api.4chan.org/b/" + str(x) + ".json" for x in range(0,16) ]
jsons = [ loads(requests.get(url).text) for url in urls ]
print "Got", len(jsons), "indexes."
# FORMAT:
# print jsons[0]['threads'][0]['posts'][0]['no']

#### Save jsons:

# Get a timestamp like '2013-01-28_03:06':
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
# Make client:
connection = Connection('localhost', 27017)
# Use database:
db = connection['4chan']
# Use collection named after the timestamp:
collection = db[now]
# Bulk insert all jsons:
collection.insert(jsons)
print now, "Inserted", collection.count(), "documents (jsons)."
# Close database connection:
connection.close()

