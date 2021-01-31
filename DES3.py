#this class dael with 3Des decrypt and encryptimport os
from Crypto.Cipher import DES3
from random import SystemRandom


class DES3():
    def __init__(self, pasword, data):
        self.key = pasword
         #check if there is not key
        self.data = data

    def _make_des3_encryptor(self, iv):
        encryptor = DES3.new(self.key, DES3.MODE_CBC, iv)
        return encryptor

    def des3_encrypt(self):
        rand = SystemRandom()
        iv = rand.getrandbits(64)
        encryptor = self._make_des3_encryptor(self.key, iv)
        pad_len = 8 - len(self.data) % 8
        #length of padding
        padding = chr(pad_len) * pad_len
        #PKCS5 padding content
        self.data += padding
        return encryptor.encrypt(self.data), iv

    def des3_decrypt(self, iv):
        encryptor = self._make_des3_encryptor(self.key, iv)
        result = encryptor.decrypt(self.data)
        pad_len = ord(result[-1])
        result = result[:-pad_len]
        return result

