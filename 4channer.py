#!/usr/bin/python
from json import loads
from glob import glob
posts = [ loads(open(x, 'r').read()) for x in glob("*json") ]
print [ x['posts'][0]['tim'] for x in posts ]
#printable = [ x['posts'][0]['tim'] for x in posts ]
### posts2 = list(postsdb.find())

### posts2[0]['posts'][2]['time']
### =>
### 1351706336

### posts2[0]['posts'][0].keys()
### => 
### [u'now', u'name', u'no', u'tn_w', u'h', u'tn_h', u'fsize', u'filename', u'tim', u'ext', u'resto', u'w', u'time', u'sticky', u'com', u'id', u'md5', u'closed']
### [u'name', u'no', u'resto', u'time', u'now', u'com', u'id']







