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

# Main entry untuk program Hack Log # 
#2019 Hacktivist Group

pilihan = None
print("======  H|4|C|K  L|0|G  ======")
print("------ Hacking Tools ------\n")
print("*Ketik '-help' untuk menampilkan pilihan dalam tools ini ")
while(True):
	pilihan = raw_input("> ")
	if pilihan == "dictionary":
		library_fungsi.webHack()
	elif pilihan == "-help":
		library_fungsi.showAllHelp()
	elif pilihan == "sql":
		library_fungsi.sqlHack()
	elif pilihan == "quit" or pilihan == "exit" or pilihan =="keluar":
		sys.exit()
