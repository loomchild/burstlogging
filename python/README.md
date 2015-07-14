# BurstLogging

## Installation
The package is on PyPI, to install it type:

    pip install burstlogging

## Usage
All you need to do is to create and configure a BurstHandler decorator 
(only _target_ is necessary, other parameters are optional and their default 
values are shown below):

	BurstHandler(target=handler, 
			level=logging.NOTSET, emitLevel=logging.INFO, burstLevel=logging.ERROR,
			capacity=1000, threshold=0.8)

Where:
* _target_ - actual handler that will format the logs; note that it will also
  filter them based on its own level
* _level_ - log level to be emitted only during burst
* _emitLevel_ - log level to be always emitted
* _burstLevel_ - log level to cause a burst
* _capacity_ - size of a log buffer; when it's too small then some debug 
  logs may be lost, when it's too big logs will be emitted with a delay
* _threshold_ - part of buffer to be purged on overflow; smaller value
  increases performance, but may cause some debug logs to be lost

See a complete example in [demo.py](demo.py).

