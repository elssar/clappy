#!/usr/bin/python

from distutils.core import setup

setup(name= 'clappy',
    version= '0.1',
    author= 'elssar',
    author_email= 'elssar@altrawcode.com',
    py_modules= ['clappy.py',],
    url= 'https://github.com/elssar/clappy',
    licence= 'MIT',
    description= 'Simple command line arguments parser.',
    long_description= open('README.md').read(),
)
