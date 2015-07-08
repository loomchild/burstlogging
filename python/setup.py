import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "burstlogging",
    version = "0.1",
    author = "Jarek Lipski",
    author_email = "pub@loomchild.net",
    description = ("Burst logging library."),
    license = "MIT",
    keywords = "logging",
    url = "https://github.com/loomchild/burstlogging",
    py_modules=['burstlogging'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

