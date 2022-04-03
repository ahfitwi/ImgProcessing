#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:56:11 2019

@author: alem
"""

import time
#from statsd import StatsClient

#statsd = StatsClient()

start = time.time()
time.sleep(3)
end=time.time()
# You must convert to milliseconds:
dt = int((end - start) * 1000)
#statsd.timing('slept', dt)