#this class deal with the connection between the user and the kind of the decryption the user want
import DES
import AES
import Keysdatabase
from START import DES3
import files_tr


class Decode():
    def __init__(self, key, algorithm, file_name, user):
        self.key = key
        self.algorithm = algorithm
        self.data = files_tr.FilesWork.read_file(file_name)
        files_tr.FilesWork.delete_file(file_name)
        self.user = user

    def ifkey(self):
        if self.key == "":
            self.key = Keysdatabase.Usersdefault.get_keydefult(self.user)
        return self.key

    def Reconaize_d(self):
        if not self.algorithm == "":
            if self.algorithm == "Des":
                newa = DES.DES(self.ifkey(), self.data, "decrypt")
                self.data = newa.decryption()
            if self.algorithm == "3DES":
                newa = DES3.DES3(self.ifkey(), self.data, "decrypt")
                self.data = newa.des3_decrypt()
            if self.algorithm == "AES":
                newa = AES.AES(self.ifkey(), self.data, "decrypt")
                self.data = newa.decrypt()
            else:
                return "error"
            return self.data
        else:
            return "error"