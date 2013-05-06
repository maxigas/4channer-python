#!/usr/bin/python
import requests
import re
pageurls = [ 'http://boards.4chan.org/b/' + str(x) for x in range(0,16) ]
pages = [ requests.get(pageurl) for pageurl in pageurls ]
#print pages[0].text
#print len(pages)
#print re.findall('p[ 0-9]{9}\" class=\"post op', pages[0].text)

def page2ids(page):
    snippets = re.findall('p[ 0-9]{9}\" class=\"post op', page.text)
    return sum([ re.findall('[0-9]{9}', snippet) for snippet in snippets ], [])

allids = [ page2ids(page) for page in pages ]

jsons = []
for idlist in allids:
    for id in idlist:
        jsons.append(requests.get('http://api.4chan.org/b/res' + id + '.json'))
        print id
#print jsons

