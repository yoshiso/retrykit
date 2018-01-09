#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from retrykit import __author__, __version__, __license__


setup(
    name='retrykit',
    version=__version__,
    description='The python retry module with context for lazy people.',
    license=__license__,
    author=__author__,
    author_email='nya060@gmail.com',
    url='https://github.com/yoshiso/retrykit.git',
    keywords='',
    packages=find_packages(),
    install_requires=[],
)
