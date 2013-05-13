#!/usr/bin/python3.2
# -*- coding: utf-8 -*-"
# Experimental parallel version of 4get.py

# JSON representations of threads and indexes:
# http(s)://api.4chan.org/**board**/res/**threadnumber**.json
# http(s)://api.4chan.org/**board**/**pagenumber**.json (0 is main index)

from joblib import Parallel, delayed
import urllib.request
from json import loads
from datetime import datetime
from pymongo import Connection

#### GET DATA!
# List of json file urls
URLS = [ "http://api.4chan.org/b/" + str(x) + ".json" for x in range(0,16) ]
# List of json files
RAWSONS = []

# Retrieve a single page and report the url and contents
def download(url, timeout=10):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

# Download jsons:
RAWSONS = Parallel(n_jobs=16)(delayed(download)(url) for url in URLS)

print("\nDownloaded %d json files (4chan indexes)." % len(RAWSONS))

#### DIGEST DATA!

# 1. .decode('utf8')
# 2. loads()
# DEBUG
# print(RAWSONS[0])
JSONS = [ loads(rawson.decode('utf-8')) for rawson in RAWSONS ]

#### SAVE SATA!

# Get a timestamp like '2013-01-28_03:06':
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
# Make client:
connection = Connection('localhost', 27017)
# Use database:
db = connection['4chan']
# Use collection named after the timestamp:
collection = db[now]
# Bulk insert all jsons:
collection.insert(JSONS)
print(now, "Inserted", collection.count(), "documents (jsons).")
# Close database connection:
connection.close()




