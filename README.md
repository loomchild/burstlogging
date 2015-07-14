# BurstLoging

## Intro

## Ports
For language specific usage see README files for individual ports:
* [Python](python/README.md)
* [Java](java/README.md)

## Details
TODO
Log debug messages in production when warning or error happened. 
Easiest implementation - store a configurable cache of messages (even debug and trace ones [cache threashold]) 
and flush them based on trigger (WARN, ERROR, FATAL).
May also temporarily enable higher level after call. 

This can result in non-chronological messages in text file, but today with multithreading, multimachine setups 
everybody should be using network logging infrastructure anyway, to allow filtering.

As appender. Need to receive all logs from loggers. Already has one level, needs a second 'burst' level. Size of cache as time and amount. 
Do not use threads, just check size before logging. Do not log anything automatically to preserve chronology. 
No risk because critical crashes will be logged immediately anyway (hence no second thread).
Appender called formatter or handler in Python.
Or maybe do not wait for INFO objects, also log them immediately and lose debug?
See MemoryHandler, flushlevel
Maybe call it contexlogging as smart is too generic
Or maybe BurstHandler?

https://docs.python.org/3.5/library/logging.handlers.html#module-logging.handlers

Use separate process aka syslog for logging that contains this smart logic.

Preserves linearity. Maybe this is not required when using a database for storing logs 
and dealing with multithreaded application where chronology does not make much sense.
