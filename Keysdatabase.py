__author__ = 'Neta'
#this class deal with all the data base- the users and the keys
import sqlite3


class Createdatabase():
    def __init__(self):
        pass

    @staticmethod
    def connect_database():
        conn = sqlite3.connect('test.db')
        print "Opened database successfully"
        return conn

    @staticmethod
    def create_tables():
        #creating the begining of the database
        conn = sqlite3.connect('test.db')
        print "Opened database successfully"

        conn.execute('''CREATE TABLE Usersdefault
                    (Username TEXT NOT NULL,
                     Defaultkey INT NOT NULL)''')

        conn.execute('''CREATE TABLE Userskey
                    (UserName TEXT NOT NULL,
                    FileName TEXT NOT NULL,
                    IsDefaultkey INT NOT NULL,
                    Keys INT)''')

        conn.execute('''CREATE TABLE Users
                    (UserName TEXT NOT NULL,
                     Name TEXT NOT NULL,
                     Aga INT NOT NULL,
                     Addres TEXT,
                     Email TEXT NOT NULL,
                     Password TEXT NOT NULL)''')

        print "Table created successfully"

        conn.close()


class Usersdefault():
    def __init__(self, name, password):
        self.usern = name
        self.key = password

    def add_userinfo(self,):
    #adding a new info to the data base
        com = Createdatabase.connect_database()
        com.execute("INSERT INTO  Usersdefault(UserName,Defaultkey) \VALUES ", (self.usern, self.key))

    @staticmethod
    def get_keydefult(user):
        #this function return the key thet mach to the file
        conn = Createdatabase.connect_database()
        dkey = conn.execute("SELECT Defaultkey from Usersdefault WHERE UserName = {0} ".format(user))
        return dkey


class Keysdatabase():
    def __init__(self):
        pass

    @staticmethod
    def check_filename(user, file_name):
        #this function check if the file name is already exist
        #return true if the file exist
        conn = Createdatabase.connect_database()
        filen = conn.execute("SELECT FileName from Userskey WHERE UserName ={0}".format(user)).fetchall()
        conn.close()
        for i in filen:
            s = i[0]
            if s == file_name:
                return True
        return False

    @staticmethod
    def get_file_keyse(user, file_name):
        #this function return the key thet mach to the file
        conn = Createdatabase.connect_database()
        key = conn.execute("SELECT Key from Userskey WHERE UserName ='{0}' and FileName ='{1}'".format(user, file_name))
        conn.close()
        return key

    @staticmethod
    def add_userinfo(user, key, namefile):
        #adding a new info to the data base
        com = Createdatabase.connect_database()
        com.execute("INSERT INTO Userskey(UserName,FileName,IsDefaultkey,Keys) \
        VALUES ", (user, namefile, 0, key))
        com.close()

    def deletefile(self, name_file):
        #if the file asked to be deleted
        #put note
        #check if the logic reasonable

        pass


class USERdatabase():
    def __init__(self, name, password, age, username, address, email):
        self.usern = username
        self.address = address
        self.age = age
        self.name = name
        self.email = email
        self.passw = password

    @staticmethod
    def isexist(name):
        #check if the username allready exist
        #return True if the username is exist
        conn = Createdatabase.connect_database()
        names = conn.execute("SELECT UserName from Users").fetchall()
        conn.close()
        for i in names:
            if i == name:
                return True
        return False

    def user_registration(self):
        #add a user to the system
        #return true if the registration work
        if not self.isexist(self.name):
            com = Createdatabase.connect_database()
            com.execute("INSERT INTO Userskey(UserName,Name,Age,Address,Password,Email)"
                        "VALUES ", (self.usern, self.name, self.age, self.address, self.passw, self.email))
            com.close()
            return True
        return False

    @staticmethod
    def forget_password(emails, user_name):
        #help to chang the user password
        #return true if the email and the user name us match and enter to the system
        conn = Createdatabase.connect_database()
        if conn.execute("SELECT Password from Users WHERE UserName ='{0}' and Email ='{1}'".format(user_name, emails))\
                .fetchall()is not []:
            check = conn.execute("SELECT Password from Users WHERE UserName ='{0}' and Email ='{1}'"
                                 .format(user_name, emails)).fetchall()
            conn.close()
            return True, check[0][0]
        else:
            return False, 0

    @staticmethod
    def login(username, password):
        #enter again
        #return true if their is a user like this
        conn = Createdatabase.connect_database()
        if conn.execute("SELECT * from Users WHERE UserName ='{0}' and Password ='{1}'".format(username, password))\
                .fetchall() is not []:
            conn.close()
            return True
        conn.close()
        return False
