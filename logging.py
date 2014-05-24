#!/usr/bin/env python3
# encoding: utf-8
"""
Logging module.
"""

import sys
import datetime
from os.path import join, abspath

log_file = '/tmp/ranger.log'

cur_file = '<Not given>'
cur_pckg = '<Not given>'

def logg(*st):
    with open("/tmp/ranger.log", 'a') as myfile:
        ban1 = ban2  = ('-FILE: ' + cur_file).ljust(60)
        ban1 += ('   PCKG: ' + cur_pckg).ljust(25)
        ban2 += ''.ljust(25)
        for i,cs in enumerate(st):
            myfile.write((ban1 if i==0 else ban2) + str(cs) + '\n')

def header(*st):
    with open(log_file, 'a') as myfile:
        myfile.write('\n\n' + '-'*30 + '\n' + str(datetime.datetime.now())
            + '\n' + '-'*30 + '\n')

def logg_modules():
    logg('[ MODULES ]', *[ a for (a,b) in globals().items() if 'module' in str(b) ])

def logg_sys_path():
    logg('[ sys.path ]', *sys.path)

def logg_dir():
    logg('[ dir() ]', *dir())

