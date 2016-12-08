#!/usr/bin/env python3
import requests
import sys
import os

from io import BytesIO
from PIL import Image

r = requests.post('http://api.everfilter.me/filters/shinkai?nightscape=0', files={'media': open(sys.argv[1], 'rb')})
image_name = 'shinkai_' + sys.argv[1]
i = Image.open(BytesIO(r.content))
i.save(image_name)
