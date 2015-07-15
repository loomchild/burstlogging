# BurstLoging

## Intro
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment without polluting the log file 
with unnecessary messages.
During normal operation only informational messages are emitted. 
However, when an error occurs, previously gathered debug messages are emitted 
as well (burst mode).

## Ports
For language specific usage see README files for individual ports:
* [Python](python/README.md)
* [Java](java/README.md)

## Details
Not much risk because critical crashes will be logged immediately anyway.

## Ideas

Preserves linearity. Maybe this is not required when using a database for storing logs 
and dealing with multithreaded application where chronology does not make much sense.

Could potentially log debug messages also after an error to give a complete context.

Use separate process communicating over a socket like syslog to become 
crash resistant and language independent.

Specify context as number of seconds instead of number of messages
