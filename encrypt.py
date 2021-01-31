#this class deal with the connection between the user and the kind of the encryption the user want
from START import DES3
import DES
import AES
import Keysdatabase
import files_tr


class Encrypt():
    def __init__(self, key, algorithm, file_name, user):
        self.key = key
        self.algorithm = algorithm
        self.data = files_tr.FilesWork.read_file(file_name)
        files_tr.FilesWork.delete_file(file_name)
        self.user = user

    def reconaize_e(self):
        if not self.algorithm == "":
            if self.algorithm == "Des":
                newa = DES.DES(self.ifkey(), self.data)
                self.data = newa.encryption()
            if self.algorithm == "3DES":
                newa = DES3.DES3(self.ifkey(), self.data)
                self.data = newa.des3_encrypt()
            if self.algorithm == "AES":
                newa = AES.AES(self.ifkey(), self.data)
                self.data = newa.encrypt()
            else:
                return "error"
            return self.data
        else:
            return "error"

    def ifkey(self):
        if self.key == "":
            self.key = Keysdatabase.Usersdefault.get_keydefult(self.user)
        return self.key
