import optparse
import hashlib
from termcolor import colored
from termcolor import cprint

parser = optparse.OptionParser()
parser.add_option('-c', '--crack', action="store", dest="md5_hash", help="MD5 salted hash to be crack")
parser.add_option('-w', '--wordlist', action="store", dest="wordlist", help="Wordlist for crack salted hash")
parser.add_option('-s', '--salt', action="store", dest="salt", help="salt value for password hash")

options, args = parser.parse_args()
if not options.md5_hash:
    print "[+] Specify a MD5 hash"
    print "[+] Example usage crack_pass.py -c hash -w /path-wordlist -s salte_value"
    print "[+] Setup the variable TIME with an appropriate time, because this sql injection is a time based."
    exit()

output = ""
md5_hash = options.md5_hash
salt = options.salt
wordlist = options.wordlist


wordlist_tmp = "/usr/share/wordlists/rockyou.txt"
salt_tmp = '58879911b02ed232'

if not options.wordlist :
    wordlist = wordlist_tmp

if not options.salt :
    salt = salt_tmp

def crack_password():
    global md5_hash
    global output
    global wordlist
    global salt
    dict = open(wordlist)
    for line in dict.readlines():
        line = line.replace("\n", "")
        beautify_print_try(line)
        if hashlib.md5(str(salt) + line).hexdigest() == md5_hash:
            output += "\n[+] Password cracked: " + line
            print output
            break
    dict.close()

def beautify_print_try(value):
    global output
    global md5_hash
    global output
    global wordlist
    global salt
    print "\033c"
    cprint('[+] MD5 hash : '+ md5_hash, 'green', attrs=['bold'])
    cprint('[+] Salt Value : ' + salt , 'green', attrs=['bold'])
    cprint('[+] Wordlist used : ' + wordlist, 'green', attrs=['bold'])
    cprint('[*] Try: ' + value, 'red', attrs=['bold'])

crack_password()