#!/usr/bin/env python

from __future__ import print_function

import logging
import sys
import re
from logging import Handler, NullHandler
from collections import deque


DEFAULT_CAPACITY = 1000
DEFAULT_THRESHOLD = 0.8

class BurstHandler(Handler):

    def __init__(self, target=NullHandler(), emitLevel=logging.INFO, 
            burstLevel=logging.ERROR, level=logging.NOTSET, 
            capacity=DEFAULT_CAPACITY, threshold=DEFAULT_THRESHOLD):
        logging.Handler.__init__(self, level)
        self.target = target
        self.emitLevel = emitLevel
        self.burstLevel = burstLevel
        self.capacity = capacity
        self.threshold = threshold
        self.buffer = deque()

    def trim(self, size):
        if len(self.buffer) > size:
            self.acquire()
            try:
                size = int(size * self.threshold)
                while len(self.buffer) > size:
                    record = self.buffer.popleft()
                    if record.levelno >= self.emitLevel:
                        self.target.handle(record)
            finally:
                self.release()

    def burst(self):
        record = self.buffer[-1]

        if record.levelno >= self.burstLevel:
            self.acquire()
            try:
                while len(self.buffer) > 0:
                    record = self.buffer.popleft()
                    self.target.handle(record)
            finally:
                self.release()

    def emit(self, record):
        self.buffer.append(record)
        self.trim(self.capacity)
        self.burst()
         
    def flush(self):
        self.trim(0)
 
    def close(self):
        self.flush()
        self.acquire()
        try:
            self.target = NullHandler()
            Handler.close(self)
        finally:
            self.release()


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    handler = logging.StreamHandler()
    handler.setLevel(logging.NOTSET)

    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    bhandler = BurstHandler(target=handler, emitLevel=logging.INFO, burstLevel=logging.ERROR, capacity=4)
    logger.handlers = []
    logger.addHandler(bhandler)

pattern = re.compile(r'.*(DEBUG|INFO|WARNING|ERROR|CRITICAL)')

#TODO: add mapping of different names for different languages
levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

def get_level(line):
    #TODO: match only part of the line to speed things up?
    match = pattern.match(line)
    if match:
        return levels.get(match.group(1))

def main():
    #TODO: maybe do not use logging to optimize things
    #OTOH this more flexible, allows logging to pipe, etc
    #duplicates formatting effort
    configure_logging()
    logger = logging.getLogger()

    while True:
        #Use readline to avoid read buffer
        line = sys.stdin.readline()
        if not line: break # EOF
        line = line.rstrip('\r\n')
        level = get_level(line)
        if level:
            logger.log(level, line)
        else:
            print(line)
            sys.stdin.flush()

if __name__ == "__main__":
    main()
