
#-*- coding: utf-8 -*-

#遍历目录或者读取文件，目录或者文件名通过参数传递进来
from sys import argv

import os

script, file = argv

if os.path.exists(file) == False:
	print "Sorry The file[%s] is Not Exist!" %file
elif os.path.isfile(file):
	print "\nThis Is A File, Start Read [%s]:" %file
	print "-" * 100
	print "File Content:"
	fd = open(file)
	print fd.read()
	print "-" * 100
	print "\n\n\n"
elif os.path.isdir(file):
	print "\nThis Is A Directory, Start List [%s]:" %file
	print "-" * 100
	print "File List:"
	for filename in os.listdir(file):
		print filename
	print "-" * 100
	print "\n\n\n"
else:
	print "\nUnknow File Type!\n"
	

