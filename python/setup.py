#!/usr/bin/env python

import os
from setuptools import setup

setup(
    name = "burstlogging",
    version = "0.2",
    author = "Jarek Lipski",
    author_email = "pub@loomchild.net",
    description = ("Burst logging library."),
    license = "MIT",
    keywords = "logging",
    url = "https://github.com/loomchild/burstlogging",
    py_modules=['burstlogging'],
    long_description="""
BurstLogging is a smart logging library that allows emitting detailed
debug information in production environment only when needed.

See project website https://github.com/loomchild/burstlogging for more details.
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

