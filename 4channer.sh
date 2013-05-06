#!/bin/bash
rm -rf boards*
seq 0 15 | parallel --progress -j 20 wget -q -p http://boards.4chan.org/b/{}
rgrep -E -o 'p[ 0-9]{9}\" class=\"post op' boards.4chan.org > /tmp/pages.html
egrep -o '[0-9]{9}' /tmp/pages.html > /tmp/ids.lst
egrep -o '/[ 0-9]+' /tmp/pages.html | sed 's|/||' > /tmp/pages.lst

# URL syntax: http://api.4chan.org/b/res/$ID
cat /tmp/ids.lst | parallel --progress -j 30 wget --quiet http://api.4chan.org/b/res/{}.json
date
echo "NUMBER OF IDS:" `wc -l /tmp/ids.lst`
#echo "NUMBER OF PAGES:"
#wc -l /tmp/pages.lst
#echo READY!
