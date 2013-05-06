#!/usr/bin/python
from matplotlib import pyplot as plt
from json import loads
from glob import glob
from pymongo import Connection
posts = [ loads(open(x, 'r').read()) for x in glob("*json") ]
mongoids = [ posts[x]['posts'][0]['no'] for x in range(0,len(posts)) ]
mongoposts = []
for mongoid, post in map(None, mongoids, posts):
    mongoposts.append({'_id': mongoid, 'posts': post['posts']})

db = Connection()
# We drop the database:
db.drop_database('channer')
# We define a variable which is a database connection to the 'chan' collection.
db = Connection().channer.chancollection
# We insert posts into the collection:
db.insert(mongoposts)
# We define a variable with the documents in the collection:
posts2 = list(db.find())


#replytimes = [ []  ]
number_of_replies = [ len(posts2[x]['posts']) - 1 for x in range(0,len(posts2))]
average_number_of_replies = sum(number_of_replies) / len(number_of_replies)
axis_x = range(1,len(number_of_replies)+1)
axis_y = number_of_replies
fig = plt.figure()
graph = fig.add_subplot(111)
graph.plot_date(axis_x, axis_y)
graph.grid(True)
plt.show()


# We generate graph:


# Drop database:
#db.drop_database('mydatabase')
# Drop collection:
# c['mydatabase'].drop_collection('mycollection')












#printable = [ x['posts'][0]['tim'] for x in posts ]
### posts2 = list(postsdb.find())

### posts2[0]['posts'][2]['time']
### =>
### 1351706336

### posts2[0]['posts'][0].keys()
### => 
### [u'now', u'name', u'no', u'tn_w', u'h', u'tn_h', u'fsize', u'filename', u'tim', u'ext', u'resto', u'w', u'time', u'sticky', u'com', u'id', u'md5', u'closed']
### [u'name', u'no', u'resto', u'time', u'now', u'com', u'id']


# import pymongo
# from pymongo import Connection

# We make a database connection and we open a collection:
# db = Connection().postsdb

# We define a python variable which is the collection:
# postsdb = db.postsdb

# We insert posts into the collection:
# postsdb.insert(posts)
# posts2 = list(postsdb.find())
# print posts2










