#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='snapgroups',
    version='0.1',
    description='Implementation of Snapchat Groups in Python',
    long_description=open('README.md').read(),
    author='Justin Brower',
    author_email='jbrower95@gmail.com',
    url='https://github.com/jbrower95/snapchatgroups',
    scripts=['brunonia.py'],
    install_requires=[
        'docopt>=0.6',
        'pycrypto>=2.6',
        'requests>=2.0'
    ],
    license=open('LICENSE').read()
)
