#!/usr/bin/python
# -*- coding: utf-8 -*-"
from pymongo import Connection as mongo
from itertools import count as count
from types import IntType as IntType
import matplotlib.pyplot as plt

# Open database connnection:
m = mongo()
# Use database:
db = m['4chan']
collectionnames = db.collection_names()
collections = [ db[collectionname] for collectionname in collectionnames ]
del collections[0] # this was the system index
documents = [ tuple(collection.find()) for collection in collections ]
# Close database connection:
m.close()

replies = []
for document in documents:
    for t in document:
        for thread in t['threads']:
            replies.append(thread['posts'][0]['replies'])

print "Number of replies:", len(replies)
replies.sort()
print "Most replies in any thread:", replies[-10:-1]

plt.plot(replies)
plt.ylabel('Number of replies')
plt.show()

