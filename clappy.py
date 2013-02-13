#!/usr/bin/python -B
#
# 

from sys import argv
from inspect import isfunction

class Parser:
    def __init__(self):
        self.args_dict= {}
    def add_arg(self, function, arguments, **kwargs):
        try:
            assert isinstance(arguments, tuple), 'Arguments should be in a tuple'
            assert isfunction(function) or function is None, 'Either pass a function, or pass None as the first argument'
            for arg in arguments:
                self.args_dict[arg]= {'func': function}
            return function
        except AssertionError, e:
            print e
    def Parse(self):
        try:
            for arg in argv[1:]:
                if arg not in self.args_dict:
                    raise Exception('Invalid argument(s). Please try again')
                
        except Exception, e:
            print e
    def args(self):
        return argv[1:]
