#-*- coding: utf-8 -*-

#遍历目录，目录通过运行参数输入

from sys import argv

import os

script, dir = argv

if os.path.exists(dir) == False:
	print "Sorry The Dir[%s] is Not Exist!" %dir
else:
	print "Start List File In Directory[%s] :" %dir
	
	for filename in os.listdir(dir):
		print filename
