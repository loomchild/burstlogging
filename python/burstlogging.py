#!/usr/bin/env python

import logging
from logging import Handler, NullHandler
from collections import deque

DEFAULT_CAPACITY = 1000
DEFAULT_THRESHOLD = 0.8

class BurstHandler(Handler):

    def __init__(self, capacity=DEFAULT_CAPACITY, threshold=DEFAULT_THRESHOLD, 
            normalLevel=logging.NOTSET, burstLevel=logging.ERROR, 
            target=NullHandler):
        logging.Handler.__init__(self, logging.NOTSET)
        self.capacity = capacity
        self.threshold = threshold
        self.normalLevel = normalLevel
        self.burstLevel = burstLevel
        self.target = target
        self.buffer = deque()
        #TODO: check if target level is >= level, raise exception if not
        #TODO: check that burst >= level
        #TODO: target should be NullHandler by default

    def trim(self, size):
        if len(self.buffer) > size:
            self.acquire()
            try:
                size = int(size * self.threshold)
                while len(self.buffer) > size:
                    record = self.buffer.popleft()
                    if record.levelno >= self.normalLevel:
                        self.target.handle(record)
            finally:
                self.release()

    def burst(self):
        record = self.buffer[-1]

        if record.levelno >= self.burstLevel:
            self.acquire()
            try:
                #TODO: optimize, maybe no multiple pops
                while len(self.buffer) > 0:
                    record = self.buffer.popleft()
                    self.target.handle(record)
            finally:
                self.release()

    def emit(self, record):
        self.buffer.append(record)
        
        self.trim(self.capacity)
        
        self.burst()
         
    def close(self):
        self.trim(0)
        self.acquire()
        try:
            self.target = NullHandler()
            Handler.close(self)
        finally:
            self.release()

