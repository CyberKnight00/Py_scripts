#!/bin/env python3
from argon2 import PasswordHasher
import threading
import time
import sys,os
import optparse
from termcolor import colored,cprint

start = time.time()

def check(word):
    try:
        if(ph.verify(hash, word) == True) :
        	cprint("{0} -> {1} ".format(hash,word),'green', attrs=['bold'])
        	print("Total time taken : {}".format(time.time() - start))
        	os._exit(1)
	else:
		# For verbose output
		cprint("{0} x-> {1} is not valid.".format(hash,word),'red', attrs=['bold']) 
        
    except :
    	# For verbose outpute
        cprint("{0} x-> {1} is not valid.".format(hash,word),'red', attrs=['bold']) 
        pass


if __name__ == '__main__':
	
	parser = optparse.OptionParser()
	parser.add_option('-c', '--crack', action="store", dest="argon2_hash", help="Argon2 hash to be crack")
	parser.add_option('-w', '--wordlist', action="store", dest="wordlist", help="Wordlist for crack salted hash")

	options, args = parser.parse_args()

	if not options.argon2_hash:
	    cprint("[+] Specify a Argon2 hash",'red', attrs=['bold'])
	    cprint("[+] Example usage crack_Argon2.py -c argon2_hash -w path-of-wordlist",'yellow', attrs=['bold'])
	    exit()
	
	else:
		hash = options.argon2_hash

	wordlist_tmp = '/usr/share/wordlists/fasttrack.txt'

	if not options.wordlist :
		wordlist = wordlist_tmp

	else:
		wordlist = options.wordlist

	ph = PasswordHasher()
	
	with open (wordlist, 'r', encoding='Latin-1') as list:
	    for word in list.read().splitlines():
	        t = threading.Thread(target=check, args=(word,))
	        t.start()

	    cprint("plain text not found !!!",'red', attrs=['bold'])
