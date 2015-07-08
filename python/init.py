import logging
import burstlogging

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

handler = logging.StreamHandler()
handler.setLevel(logging.NOTSET)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

bhandler = burstlogging.BurstHandler(target=handler, normalLevel=logging.INFO, burstLevel=logging.ERROR, capacity=4)
logger.handlers = []
logger.addHandler(bhandler)
