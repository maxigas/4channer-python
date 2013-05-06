#!/usr/bin/python
import requests
from pymongo import Connection
from multiprocessing import Pool
p = Pool(10)
pageurls = [ 'http://api.4chan.org/b/' + str(board) + '.json' for board in range(0,16) ]
pages = [ requests.get(pageurl).json for pageurl in pageurls  ]
allthreadids = [ page['threads'][thread]['posts'][0]['no'] for page in pages for thread in range(0,len(page['threads']))]
threadurls = [ 'http://api.4chan.org/b/res/' + str(threadid) + '.json' for threadid in allthreadids ]
#threads = [ requests.get(threadurl).json for threadurl in threadurls ]
#threads = [ for threadurl in threadurls:
#    print threadurl
#    requests.get(threadurl) ]

counter = 0
threads = []
def threadurl2thread(threadurl):
    global counter
    counter = counter + 1
    print counter
    threads.append(requests.get(threadurl))

p.map(threadurl2thread, threadurls[0:10])

db = Connection()

db.drop_database('channer')

db = Connection().channer.chancollection

db.insert(threads)

threads2 = list(db.find())
#print threads[0]

