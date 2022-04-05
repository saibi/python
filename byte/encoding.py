#!/usr/bin/env python
# -*- coding: utf8 -*-

import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"한글한글한글한글")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print text


