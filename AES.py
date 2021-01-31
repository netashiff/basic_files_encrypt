#this class dael with Aes decrypt and encrypt
import base64
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
PAD = lambda s: s+(BS - len(s) % BS) * chr(BS - len(s) % BS)
UNPAD = lambda s: s[:-ord(s[len(s)-1:])]
BLOCK_SIZE = 128


class AESWrapper:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def encrypt(self):
         #encrypt the file with the key and aes and return the encrypt text
        new_text = PAD(self.data)
        iv = Random.new().read(AES.BLOCK_SIZE)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(new_text))

    def decrypt(self, enc):
        #decrypt the file with the key and aes and return the decrypt text
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return UNPAD(cipher.decrypt( enc[16:] ))