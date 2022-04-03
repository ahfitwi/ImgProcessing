#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:21:43 2019

@author: alem
"""

import random
r1 = random.randint(2**128, 2**256) 
print("Random number between 0 and 10 is % s" % (r1)) 
key=hex(r1)
print('key=',key)