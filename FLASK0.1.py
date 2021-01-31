#the main program that connect with the users, data base and start user interface
import Keysdatabase
import os
from flask import Flask, request, redirect, render_template, Response
from werkzeug.utils import secure_filename
import encrypt
import decoding

UPLOAD_FOLDER = 'C:\\Heights\\Documents\\the_project\START\\all_the_files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route('/')
def enter():
    #the login to the website
    return render_template('entering.html')


@app.route('/registration')
def registration():
    #new registration
    return render_template('registretion.html')


@app.route('/start')
def show_user_profile():
    # show the user profile for that user
    return render_template('start.html')


@app.route('/working', methods=['POST'])
def start_work():
    what_needed = request.form["ch"]
    # check if the post request has the file part
    if 'file' not in request.files:
        print "No file part"
        return redirect('/error', code=302)
        #to write error
    filew = request.files['file']
    print filew
    # if user does not select file, browser also
    # submit a empty part without filename
    if filew.filename == '':
        print('No selected file')
        return redirect('/error', code=302)
    if file and allowed_file(filew.filename):
        filename = secure_filename(filew.filename)
        filew.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if what_needed == "encrypt":
            key = request.form["key"]
            selected_encrypt = request.form["kind encrypt"]
            return download_file(encrypt.Encrypt(key, selected_encrypt, filename, "chhoose how to enter the user name"))
        if what_needed == "decrypt":
            key = request.form.get["key"]
            selected_encrypt = request.form["kind encrypt"]
            return download_file(decoding.Decode(key, selected_encrypt, filename, "chhoose how to enter the user name"))


@app.route('/download')
def download_file(data):
    return Response(data,
                    mimetype="text/plain",
                    headers={"Content-Disposition": "attachment;filename=test.txt"})


@app.route('/Error', methods=['POST'])
def send_error():
    #send error to the user enter the incorrect
    return redirect('/start', code=302)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if Keysdatabase.USERdatabase.login(username, password):
        return redirect('/start', code=302)
    else:
        return redirect('/loginError', code=302)


@app.route('/loginError', methods=['POST'])
def send_login_error():
    #send error to the user if the user name or the password you entered is incorrect
    return redirect('/login', code=302)


@app.route('/nameError', methods=['POST'])
def send_name_error():
    #send error to the user if his name all ready exist
    return redirect('/registration', code=302)


@app.route('/tryR', methods=['POST'])
def registration_user():
    username = str(request.form["username"])
    password = str(request.form["password"])
    name = str(request.form["first name"])+" " + str(request.form["last name"])
    address = str(request.form["address"])
    email = str(request.form["email"])
    age = int(request.form["age"])
    print username, password, name, address, email
    if not Keysdatabase.USERdatabase.isexist(username):
        #check if thr user name is available
        user1 = Keysdatabase.USERdatabase(name, password, age, username, address, email)
        #name, password, age, username, address, email
        if user1.user_registration():
            #registration thr user in the data base
            #needed to save password
            return redirect('/start', code=302)
    else:
        return redirect('/nameError', code=302)


if __name__ == "__main__":
    if not os.path.exists("C:\\Heights\\Documents\\the_project\\START\\test.db"):
        new = Keysdatabase.Createdatabase()
        new.create_tables()
    app.run()