#!/usr/bin/env python

import sys
sys.path.append("..")

import time
import logging
import burstlogging


print("Configure logging")
logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

handler = logging.StreamHandler()
handler.setLevel(logging.NOTSET)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

bhandler = burstlogging.BurstHandler(target=handler, emitLevel=logging.INFO, burstLevel=logging.ERROR, capacity=4)
logger.handlers = []
logger.addHandler(bhandler)

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

