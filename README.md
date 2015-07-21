# BurstLoging

## Intro
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment without polluting the log file 
with unnecessary messages.
During normal operation only informational messages are logged. 
However, when an error occurs, previously gathered debug messages are logged 
as well.

## Ports
For programming language specific usage see README files for individual ports:
* [Python](python/README.md)
* [Java](java/README.md)(work in progress)

## Details 
Logging is always a compromise between storing everything and saving disk space / performance. 

Some errors occur only in production or are very difficult to reproduce. 

BurstLogging tries to log debug messages only when they are needed. 

It works by temporarily keeping all logs in a buffer. When an error occurs they are dumped.  

When an error doesn't occur only informational messages are logged and old debug messages are dropped.

Immediate risk when buffering log messages is the program crashing before being able to store them. 
The problem is not critical because recognised error condition triggers an immediate dump. 
Danger can be further reduced by running the logging system in a separate process and listening on a socket 
(see enhancement #5 (https://github.com/loomchild/burstlogging/issues/5)).

BurstLogging preserves chronological order of messages by dropping debug messages that are older than the logged message. 
This feature may not be required when logs are stored in a database instead of a flat file. 
Chronological order also does not make much sense when dealing with multithreaded application.

## Ideas
This is a relatively new constantly evolving project. To see and discuss ideas see
[enhancements](https://github.com/loomchild/burstlogging/labels/enhancement).
