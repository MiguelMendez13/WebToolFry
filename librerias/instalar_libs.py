#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
	from bs4 import BeautifulSoup
except Exception, e:
	if "cannot import name BeautifulSoup" in e:
		os.chdir("beautifulsoup")
		os.system("python setup.py install")
		print "Se instalo bs4 Correctamente"
		os.chdir("..")
try:
	import mechanize
except Exception, e:
	print e
	if "No module named mechanize" in e:
		os.chdir("mechanize")
		os.system("python setup.py install")
		print "Se instalo mechanize Correctamente"
		os.chdir("..")
try:
	import wx
except Exception, e:
	print e
	if "No module named wx" in e:
		print "No esta instalada la libreria wx Link de descarga: http://www.wxpython.org/download.php" 