#!/usr/bin/env python
import ambiltag
import requests
import string
import time
import library_fungsi
import sys
# import urllib
# import re
# from bs4 import BeautifulSoup

pilihan = None
print("------ Aplikasi hacking webserver ------")
print("*Ketik '-help' untuk menampilkan pilihan dalam tools ini ")
while(True):
	pilihan = raw_input("> ")
	if pilihan == "web-hack":
		library_fungsi.webHack()
	elif pilihan == "-help":
		library_fungsi.showAllHelp()
	elif pilihan == "quit" or pilihan == "exit" or pilihan =="keluar":
		sys.exit()
