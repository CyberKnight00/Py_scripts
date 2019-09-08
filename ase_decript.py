import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

key = "Key to decript"
enc = "AES encoded HASH"
key = hashlib.md5(key.encode()).hexdigest()

print "Key = " + key

enc = base64.b64decode(enc)
cipher = AES.new(key,AES.MODE_ECB)
print "Decoded : \n" + cipher.decrypt(enc).decode("utf-8")