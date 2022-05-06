from email.mime import image
from flask import Flask, redirect, send_from_directory, request
import random
import glob
import json
import sqlite3

app = Flask(__name__)

#admin, user or none
userType = "none"

# Path for our main Svelte page
@app.route("/")
def base():
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
    myConnection = sqlite3.connect('tkinter/usersList.sqlite')
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
             
            
    # check if user exists in database with correct password => return type of user, else => return error info
    

@app.route("/signUp", methods=["POST"])
def signUp():
    contains = False
    myConnection = sqlite3.connect('tkinter/usersList.sqlite')
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

@app.route("/logOut", methods=["POST"])
def logOut():
    global userType
    userType = "none"
    return userType

if __name__ == "__main__":
    app.run(debug=True)
