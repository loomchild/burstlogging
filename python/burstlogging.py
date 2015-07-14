import logging
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
        #TODO: check if target handler level is >= level
        #TODO: check that burstLevel >= emitLevel >= level

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

