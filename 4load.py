#!/usr/bin/python
# -*- coding: utf-8 -*-"
from pymongo import Connection
from itertools import count as count
from types import IntType as IntType
import matplotlib.pyplot as plt

# Open database connnection:
connection = Connection()
# Use database:
db = connection['4chan']
collectionnames = db.collection_names()
collections = [ db[collectionname] for collectionname in collectionnames ]
del collections[0] # this was the system index
documents = [ list(collection.find()) for collection in collections ]
# Close database connection:
connection.close()

replies = []
for document in documents:
    for index in document:
        for thread in index['threads']:
            replies.append(thread['posts'][0]['replies'])

print "Number of collections:", len(collections)
print "Number of documents:", len(documents)
print "Number of replies:", len(replies)
replies.sort()
print "10 highest replies in any thread:", replies[-10:-1]

plt.plot(replies)
plt.ylabel('Number of replies')
plt.show()

