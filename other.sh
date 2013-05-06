#!/bin/bash
for i in {1..16};
do
    wget -q -p http://boards.4chan.org/b/$i&
done
wait
rgrep -E -o 'p[  0-9]{9}\" class=\"post op' . > /tmp/pages.html
egrep -o '[ 0-9]{9}' /tmp/pages.html . > /tmp/ids.lst
egrep -o '/[ 0-9]+' /tmp/pages.html | sed 's|/||' > /tmp/pages.lst
# URL syntax: http://api.4chan.org/b/res/$ID
cat /tmp/ids.lst #| parallel "wget --quiet http://api.4chan.org/b/res/{}.json &"
wait
echo READY!
wc -l /tmp/ids.lst
wc -l /tmp/pages.lst