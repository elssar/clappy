#!/usr/bin/python

# Test file for Clappy

import clappy

parser= clappy.Parser()

@parser.add_arg(('-a', '--argh'))
def test1():
    """Test function 1"""
    print 'It works!'
test2= parser.add_arg(None, ('-t'), help= 'Test 2')
if '-t' in parser.args_dict:
    print 'Success'
@parser.add_arg(('-f'), n= 2)
def test3(a, b):
    """Test function 3"""
    print a, b, 'So far, so good'
@parser.add_arg(('-p'), n='0, 3')
def test4(*args):
    print args, 'Looks good!'
parser.Parse()
