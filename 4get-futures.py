#!/usr/bin/python3.2
# -*- coding: utf-8 -*-"
# Experimental parallel version of 4get.py

# JSON representations of threads and indexes:
# http(s)://api.4chan.org/**board**/res/**threadnumber**.json
# http(s)://api.4chan.org/**board**/**pagenumber**.json (0 is main index)

import concurrent.futures, urllib.request
from json import loads
from datetime import datetime
from pymongo import Connection

# List of json file urls
URLS = [ "http://api.4chan.org/b/" + str(x) + ".json" for x in range(0,16) ]
# List of json files
JSONS = []

# Retrieve a single page and report the url and contents
def load(url, timeout):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

# Download the json files
with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load, url, 10): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
#           DEBUG:
#            print('%r page is %d bytes' % (url, len(data)))
            JSONS.append(loads(data.decode('utf-8')))
#           DEBUG:
#            print('.', end='')

print("\nDownloaded %d json files (4chan indexes)." % len(JSONS))

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
collection.insert(JSONS)
print(now, "Inserted", collection.count(), "documents (jsons).")
# Close database connection:
connection.close()




