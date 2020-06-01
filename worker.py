# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:14:17 2020

@author: agach
"""

import threading

class Worker(threading.Thread):
    # Our workers constructor, note the super() method which is vital if we want this
    # to function properly
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(10):
           print(i)