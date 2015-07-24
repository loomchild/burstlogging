# BurstLoging

## Intro
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment without polluting the log file 
with unnecessary messages.
During normal operation only informational messages are logged. 
However, when an error occurs, previously gathered debug messages are logged 
as well.

## Installation
The package is on PyPI, to install it type:

    pip install burstlogging

## Usage

### As a separate process
This is the preferred way of using BurstLogging. 

### As a Python Log Handler
This method is an alternative method of using BurstLogging. Benefits are:
* simplicity - there is only only one process to manage
* performance - there is potentially no need to format log messages that won't be displayed (separate process 
  implementation will be improved in the future to reduce this difference)
and the drawbacks are:
* it is only available in Python programming language
* when the main process crashes some logs may be lost in the memory buffer, which will make error analysis harder

To use it all you need to do is to create and configure a BurstHandler decorator 
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

### Demos
See a complete usage examples in [demo](demo/).

## Details 
Logging is always a compromise between storing everything and saving disk space / performance. 

Some errors occur only in production or are very difficult to reproduce. 

BurstLogging tries to log debug messages only when they are needed. 

It works by temporarily keeping all logs in a buffer. When an error occurs they are dumped.  

When an error doesn't occur only informational messages are logged and old debug messages are dropped.

Immediate risk when buffering log messages is the program crashing before being able to store them. 
The problem is not that critical because recognised error condition triggers an immediate dump. 
Danger can be further reduced by running the logging system in a separate process and listening on a socket 
(see enhancement [#5](https://github.com/loomchild/burstlogging/issues/5)).

BurstLogging preserves chronological order of messages by dropping debug messages that are older than the logged message. 
This feature may not be required when logs are stored in a database instead of a flat file. 
Chronological order also does not make much sense when dealing with multithreaded application.

## Ideas
This is a relatively new constantly evolving project. To see and discuss ideas see
[enhancements](https://github.com/loomchild/burstlogging/labels/enhancement).
