#!/usr/bin/env python
import json
import urllib2
print(json.loads(urllib2.urlopen('http://miniplay.imbc.com/WebLiveURL.ashx?channel=mfm&agent=&protocol=RTMP').read()[1:-2])['AACLiveURL'])
