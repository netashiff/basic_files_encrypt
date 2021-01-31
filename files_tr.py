#the class can read and delete files
import os
PATH = 'C:\\Heights\\Documents\\the_project\START\\all_the_files'


class FilesWork:
    def __init__(self, file_name):
        self.name_file = file_name

    @staticmethod
    def delete_file(name_file):
    ## if file exists, delete it ##
        if os.path.isfile(PATH + name_file):
                os.remove(name_file)
        else:
         ## Show an error
                print("Error: %s file not found" % name_file)

    @staticmethod
    def read_file(name_file):
        with open(PATH + name_file, 'rb') as files:
            data = files.read()
        FilesWork.delete_file(name_file)
        return data