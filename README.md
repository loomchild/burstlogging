# BurstLoging

## Intro
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment without polluting the log file 
with unnecessary messages. During normal operation only informational messages are logged. 
However, when an error occurs, previously gathered debug messages are logged 
as well.

It works by temporarily keeping all log records in a buffer. It preserves 
their chronological order by dropping debug messages that are older 
than the recently logged message. There is no huge performance penalty 
because message is formatted only when it's emitted.

## Installation
The package is on PyPI, to install it type:

    pip install burstlogging

## Usage
To use BurstLogging all you need to do is to create and configure a BurstHandler decorator 
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

### Demo
See a complete usage examples in [demo.py](demo.py).

## Ideas
This is a relatively new constantly evolving project. To see, propose and discuss ideas visit
[enhancements](https://github.com/loomchild/burstlogging/labels/enhancement).
