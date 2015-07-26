#!/usr/bin/env python

import time
import logging

print("A")
import os, sys
#fifo = os.open("/tmp/test.log", os.O_RDONLY | os.O_NONBLOCK)
#sys.stderr = open("/tmp/test.log", "wt")
#os.close(fifo)
#er = sys.stderr
#fifo = os.open("/tmp/test.log", os.O_WRONLY | os.O_NONBLOCK)
#sys.stderr = os.fdopen(fifo, "wt")
#er.close()
print("B")

print("Configure logging")
logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

handler = logging.StreamHandler()
handler.setLevel(logging.NOTSET)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger.handlers = []
logger.addHandler(handler)

print("Normal operation, no errors - only INFO messages and above are emitted")
logger.debug("01 Log")
time.sleep(0.1)
logger.debug("02 Log")
time.sleep(0.1)
logger.info("03 Log")
time.sleep(0.1)
logger.debug("04 Log")
time.sleep(0.1)
logger.debug("05 Log")
time.sleep(0.1)
logger.info("06 Log")
time.sleep(0.1)
logger.debug("07 Log")
time.sleep(0.1)
logger.debug("08 Log")

print("An error occurs which causes burst; "
        + "note that although some messages are lost due to insufficient buffer capacity, " 
        + "their chronological order is maintained")
time.sleep(1)
logger.debug("09 Log")
time.sleep(0.1)
logger.debug("10 Log")
time.sleep(0.1)
logger.info("11 Log")
time.sleep(0.1)
logger.debug("12 Log")
time.sleep(0.1)
logger.debug("13 Log")
time.sleep(0.1)
logger.info("14 Log")
time.sleep(0.1)
logger.debug("15 Log")
time.sleep(0.1)
logger.error("16 Log")

for i in range(1,100000):
    time.sleep(0.001)
    if i % 100 == 0:
        print(i)
    logger.info("Log %s AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", i)
