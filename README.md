# BurstLoging

## Intro
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment without polluting the log file 
with unnecessary messages.
During normal operation only informational messages are emitted. 
However, when an error occurs, previously gathered debug messages are emitted 
as well (burst mode).

## Ports
For programming language specific usage see README files for individual ports:
* [Python](python/README.md)

## Details
Not much risk because critical crashes will be logged immediately anyway.

Preserves linearity. Maybe this is not required when using a database for storing logs 
and dealing with multithreaded application where chronology does not make much sense.

## Ideas
This is a new project. To see and discuss more ideas about burst logging see
[Enhancements](https://github.com/loomchild/burstlogging/labels/enhancement).
