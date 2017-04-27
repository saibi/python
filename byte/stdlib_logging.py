#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join('/tmp', 'test.log')


print "logging to", logging_file

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename = logging_file,
        filemode = 'w',
)

logging.debug('start of the program')
logging.info('doing something')
logging.warning('dying now')

