#!/usr/bin/env python

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
logger.debug("1 Log")
time.sleep(0.1)
logger.debug("2 Log")
time.sleep(0.1)
logger.info("3 Log")
time.sleep(0.1)
logger.debug("4 Log")
time.sleep(0.1)
logger.debug("5 Log")
time.sleep(0.1)
logger.info("6 Log")
time.sleep(0.1)
logger.debug("7 Log")
time.sleep(0.1)
logger.debug("8 Log")
time.sleep(0.1)
logger.warn("9 Log")
bhandler.flush()

print("An error occurs which causes burst; "
        + "note that although some messages are lost due to insufficient buffer capacity, " 
        + "their chronological order is maintained")
time.sleep(1)
logger.debug("1 Log")
time.sleep(0.1)
logger.debug("2 Log")
time.sleep(0.1)
logger.info("3 Log")
time.sleep(0.1)
logger.debug("4 Log")
time.sleep(0.1)
logger.debug("5 Log")
time.sleep(0.1)
logger.info("6 Log")
time.sleep(0.1)
logger.debug("7 Log")
time.sleep(0.1)
logger.error("8 Log")
bhandler.flush()

