#!/bin/env python3
from passlib.utils import pbkdf2
import binascii, sys

# usage wpa-psk-genpy <Passphrase> <SSID> 
try :
	print("PSK = ",binascii.hexlify(pbkdf2.pbkdf2(str.encode(sys.argv[1]), str.encode(sys.argv[2]), 4096, 32)).decode("utf-8"))

except:
	print("Usage wpa-psk-genpy <Passphrase> <SSID>")