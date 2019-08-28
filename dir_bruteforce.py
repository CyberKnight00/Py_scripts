#!/usr/bin/python2.7

import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

path=[]
def dirdiscover(url):
	with open("wordlist.txt","r") as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			test_url = url + "/" + word
			response = request(test_url)
			if response :
				print "[+] Discover " + test_url
				path.append(word)

url="<url>"

dirdiscover(url)

for paths in path:
	dirdiscover(url+"/"+ paths)


