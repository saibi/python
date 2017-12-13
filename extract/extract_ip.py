#!/usr/bin/env python3


# extract ip from ifconfig output

import sys
import re

with open(sys.argv[1], 'r') as f:
    for line in f:
        idx = line.find('addr:172')
        if idx >= 0:
            ipstr = line[idx+5:idx+20]
            m = re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ipstr)
            if m:
                print(m.group(0) + '\t' + 'bleedoff')
