#!/bin/bash python

import requests


def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	print(file_name)
	# print(get_response)
	# print(get_response.content)
	with open(file_name, 'wb') as out_file:
		out_file.write(get_response.content)


download('https://www.armourinfosec.com/wp-content/uploads/2015/06/cise.jpg')

