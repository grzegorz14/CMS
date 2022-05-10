from email.mime import image
from flask import Flask, redirect, send_from_directory, request
#from PIL import Image for saving slider images in directory
import glob
import sqlite3

app = Flask(__name__)

#admin, user or none
userType = "none"

# Path for our main Svelte page
@app.route("/")
def base():
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM settings")
    settings = myCursor.fetchall()
    print(settings)
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    print(path)
    return send_from_directory('client/public', path)


@app.route("/getImagesLength", methods=["POST"])
def getImagesLength():
    images = [f for f in glob.glob("./client/public/images/*")]
    print(len(images))
    return str(len(images))

@app.route("/getImage", methods=["POST"])
def getImage():
    id = request.args.get('id')
    images = [f for f in glob.glob("./client/public/images/*")]
    print(len(images))
    if int(id) < len(images):
        return str(images[int(id)])
    return "wrongId"

@app.route("/logIn", methods=["POST"])
def logIn():
    ok = False
    login = request.form["login"]
    password = request.form["password"]
    print(f"User '{login}' is trying to log in.")
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    print(users)
    for user in users:
        print(user)
        if login == user[0] and password == user[1]:
            global userType
            userType = user[2]
            ok = True
            return userType
    if ok == False:
        print("Wrong username or password!")
        return "Wrong username or password!"

@app.route("/signUp", methods=["POST"])
def signUp():
    contains = False
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    print(users)
    login = request.form["login"]
    password = request.form["password"]
    for user in users:
        if user[0] == login:
            contains = True
            return "loginAlreadyInUse"
    if contains == False:   
        print(f"Account created for user - '{login}'.")
        myCursor.execute(
            f"INSERT INTO users (login, password, permissions) VALUES ('{login}', '{password}', 'user')")
        myConnection.commit()
        # add record to database, if no problems => return accountCreated, else => return error info
        return "accountCreated"

@app.route("/getUserType", methods=["POST"])
def getUserType():
    # return admin, user or none
    return userType

@app.route("/updateLogin", methods=["POST"])
def updateLogin():
    login = request.form["login"]
    newLogin = request.form["newLogin"]
    print(login)
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for user in users:
        if user[0] == login:
            myCursor.execute(f"UPDATE users SET login = '{newLogin}', password = '{user[1]}', permissions = '{user[2]}' WHERE login = '{login}'")
            myConnection.commit()
            
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    print(users)
    myConnection.close()
    return 'Updated'
        
@app.route("/updatePassword", methods=["POST"])
def updatePassword():
    login = request.form["login"]
    newPassword = request.form["newPassword"]
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for user in users:
        if user[0] == login:
            myCursor.execute(f"UPDATE users SET login = '{login}', password = '{newPassword}', permissions = '{user[2]}' WHERE login = '{login}'")
            myConnection.commit()
            myConnection.close()
            return 'Updated'       

@app.route("/updatePermissions", methods=["POST"])
def updatePermissions():
    login = request.form["login"]
    newPermissions = request.form["newPermissions"]
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for user in users:
        if user[0] == login:
            myCursor.execute(f"UPDATE users SET login = '{login}', password = '{user[1]}', permissions = '{newPermissions}' WHERE login = '{login}'")
            myConnection.commit()
            myConnection.close()
            global userType
            userType = newPermissions
            return 'Updated'

@app.route("/deleteUser", methods=["POST"])
def deleteUser():
    login = request.form["login"]
    print(login)
    myConnection = sqlite3.connect('tkinter/database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute(f"DELETE FROM users WHERE login = '{login}'")
    myConnection.commit()
    global userType
    userType = "none"
    return "Deleted"

@app.route("/logOut", methods=["POST"])
def logOut():
    global userType
    userType = "none"
    return userType

if __name__ == "__main__":
    app.run(debug=True)
