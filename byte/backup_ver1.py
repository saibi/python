#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import time

source = ['/home/saibi/code_test/python/tutorial', '/home/saibi/code_test/python/byte']

target_dir = '/tmp'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

print "Zip command is:", zip_command
print "Running:"
if os.system(zip_command) == 0:
    print 'Successful backup to', target_dir
else:
    print 'Backup FAILED'


