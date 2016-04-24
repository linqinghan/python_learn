#-*- coding: utf-8 -*-

#遍历目录，目录名通过参数输入

from sys import argv

import os

script, dir = argv

if os.path.exists(dir) == False:
	print "Sorry The Dir[%s] is Not Exist!" %dir
elif os.path.isdir(dir) == False:
	print "%s Is Not A Directory!" %dir
else:
	print "Start List File In Directory[%s] :" %dir	
	for filename in os.listdir(dir):
		print filename

