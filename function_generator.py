#!/usr/bin/env python27

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3

od = odd()
for i in od:
	print i
