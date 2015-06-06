import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "smartlogginglevel",
    version = "0.1",
    author = "Jarek Lipski",
    author_email = "pub@loomchild.net",
    description = ("Smart logging level."),
    license = "MIT",
    keywords = "logging",
    url = "https://github.com/loomchild/smartlogginglevel",
    py_modules=['smartlogginglevel'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)

