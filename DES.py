__author__ = 'Neta'
#this class dael with des decrypt and encrypt
from Crypto.Cipher import DES
import operator


class DES:
    def __init__(self, pasword, data):
        self.pasword = pasword
         #check if there is not key
        self.data = data

    def encryption(self):
        #encrypt the file with the key and des and return the encrypt text
        des = DES.new(self.pasword, DES.MODE_ECB)
        cipher_text = des.encrypt(self.data)
        return cipher_text

    def decryption(self):
        #decrypt the file with the key and des and return the decrypt text
        des = DES.new(self.pasword, DES.MODE_ECB)
        decrypt_text = des.decrypt(self.data)
        return decrypt_text
