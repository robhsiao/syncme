#!/bin/env python2.4
import ConfigParser, sys

cf = ConfigParser.ConfigParser()
try:
    cf.read('Syncfile')
except Exception, inst:
    print >> sys.stderr, "** syncme: error format Syncfile"
    print >> sys.stderr, inst
print sys.argv[0]
for section in cf.sections():
    print cf.items(section)
