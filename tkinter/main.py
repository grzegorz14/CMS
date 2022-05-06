from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

try:
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("""CREATE TABLE users (
                       login text,
                       password text,
                       permissions text
                       )""")
    myCursor.execute(
        f"INSERT INTO users (login, password, permissions) VALUES ('admin', 'admin', 'admin')")
    myCursor.execute("""CREATE TABLE settings (
                       theme text,
                       fontSize text,
                       font text,
                       navbarColor text,
                       navbarBackgroundColor text,
                       signUpBackgroundColor text,
                       signUpBackgroundColorHover text,
                       sliderColor text,
                       newsColor text,
                       newsBackgroundColor text,
                       newsButtonColor text,
                       newsButtonBackgroundColor text,
                       newsButtonBackgroundColorHover text,
                       photosColor text,
                       photosBackgroundColor text,
                       footerColor text,
                       footerBackgroundColor text,
                       articleColor text,
                       articleBackgroundColor text,
                       articleBackgroundBackgroundColor text,
                       commentsColor text,
                       commentsBackgroundColor text,
                       commentsButtonColor text,
                       commentsButtonBackgroundColor text,
                       commentsTextareaColor text,
                       commentsTextareaBackgroundColor text,
                       commentsUsernameColor text,
                       galleryColor text,
                       galleryBackgroundColor text
                       )""")
    myCursor.execute(f"INSERT INTO settings (theme,fontSize,font,navbarColor,navbarBackgroundColor,signUpBackgroundColor,signUpBackgroundColorHover,sliderColor,newsColor,newsBackgroundColor,newsButtonColor,newsButtonBackgroundColor,newsButtonBackgroundColorHover,photosColor,photosBackgroundColor,footerColor,footerBackgroundColor,articleColor,articleBackgroundColor,articleBackgroundBackgroundColor,commentsColor,commentsBackgroundColor,commentsButtonColor,commentsButtonBackgroundColor,commentsTextareaColor,commentsTextareaBackgroundColor,commentsUsernameColor,galleryColor,galleryBackgroundColor) VALUES ('1','20','font','white','#021D47','#369dc5','#8cdeff','white','black','white','white','#40a3c4','#72bbd3','black','white','black','white','black','white','white','black','#73858b','white','#0084ff','black','white','#0084ff','black','white')")
    myConnection.commit()
except:
    print("Database already exist")

main = Tk()
main.title("Login Page")
main.geometry("300x300")

def openRoot():
    root = Tk()
    root.title("Users List")
    root.geometry("300x300")

    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for i, user in enumerate(users):
        if user[0] != 'admin':
            print(user[0])
            Label(root, text=f"Nazwa Użytkowinika: {user[0]}").grid(row=1 + i, column=0)
            def cursed(q):
                return lambda: editUserData(users[q][0], users[q][1], users[q][2])
            button = Button(root, text="Edit", command=cursed(i))
            button.grid(row=1 + i, column=1)

def openDeleteRoot():
    delete = Tk()
    delete.title("Users List")
    delete.geometry("300x300")

    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for i, user in enumerate(users):
        if user[0] != 'admin':
            print(user[0])
            Label(delete, text=f"Nazwa Użytkowinika: {user[0]}").grid(row=1 + i, column=0)
            def cursed(q):
                return lambda: deleteUserData(users[q][0], users[q][1], users[q][2])
            button = Button(delete, text="Delete", command=cursed(i))
            button.grid(row=1 + i, column=1)

def addUser(login,password,permissions):
    jest = False
    print(login,password,permissions)
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    for user in users:
        print(user[0])
        if user[0] == login:
            print("Username already in use!")
            jest = True

    if jest == False:
        myCursor.execute(
            f"INSERT INTO users (login, password, permissions) VALUES ('{login}', '{password}', '{permissions}')")
        myConnection.commit()
        myCursor.execute("SELECT * FROM users")
        users = myCursor.fetchall()
        myConnection.close()
        print(users)
        info = 'User is updated'
        jest = False
def openAddUsersPage():
    add = Tk()
    add.title("Addition Page")
    add.geometry("300x300")

    Label(add, text="Login").grid(row=0, column=0)
    login = Entry(add)
    login.grid(row=1, column=0)
    Label(add, text="Password").grid(row=2, column=0)
    password = Entry(add)
    password.grid(row=3, column=0)
    Label(add, text="Permissions").grid(row=4, column=0)
    variable = StringVar(add)
    variable.set("user")
    permissions = OptionMenu(add,variable,"user","moderator","admin")
    permissions.grid(row=5, column=0)
    Button(add, text="Edit Users", command=lambda: addUser(login.get(),password.get(),variable.get())).grid(row=0, column=1)

def adminCheck(login,password):
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    for user in users:
        if login == user[0] and password == user[1] and user[2] == 'admin':
            openDialog()
        else:
            Label(main, text="Wrong username or password!").grid(row=5, column=1)
            print("-_-")

def openDialog():
    dialog = Tk()
    dialog.title("Edition Page")
    dialog.geometry("300x300")
    Label(dialog, text="Users: ").grid(row=0, column=0)
    Button(dialog, text="Edit Users", command=openRoot).grid(row=0, column=1)
    Button(dialog, text="Delete Users", command=openDeleteRoot).grid(row=0, column=2)
    Button(dialog, text="Add Users", command=openAddUsersPage).grid(row=0, column=3)

def editUserData(login,password,permissions):
    print(login)
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for user in users:
        if user[0] == login:
            edit = Tk()
            edit.title("Edit Page")
            edit.geometry("300x300")
            Label(edit,text="Login").grid(row=0,column=0)
            newLogin = Entry(edit)
            newLogin.insert(0,login)
            newLogin.grid(row=0,column=1)

            Label(edit, text="Password").grid(row=1,column=0)
            newPassword = Entry(edit)
            newPassword.insert(0, password)
            newPassword.grid(row=1,column=1)
            Label(edit, text="Permissions").grid(row=2,column=0)
            variable = StringVar(edit)
            variable.set(permissions)
            newPermissions = OptionMenu(edit, variable, "user", "moderator", "admin")
            newPermissions.grid(row=2,column=1)
            Button(edit,text="Zapisz",command=lambda: saveData(newLogin.get(),newPassword.get(),variable.get(),str(login))).grid(row=3,column=0)

def deleteUserData(login,password,permissions):
    print(login)
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    myCursor.execute(
        f"DELETE FROM users WHERE login = '{login}'")
    myConnection.commit()


def saveData(newLogin,newPassword,newPermissions,oldLogin):

    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    # if newPassword == "" or newLogin == "" or newPassword.isspace() or newLogin.isspace():
    #     error = 'Some fields were empty, user is not updated.'

    myCursor.execute(f"UPDATE users SET login = '{newLogin}', password = '{newPassword}', permissions = '{newPermissions}' WHERE login = '{oldLogin}'")
    myConnection.commit()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    myConnection.close()
    print(users)
    info = 'User is updated'

Label(main,text="Login").grid(row=0,column=0)
login = Entry(main)
login.grid(row=1,column=0)
Label(main,text="Password").grid(row=2,column=0)
password = Entry(main)
password.grid(row=3,column=0)
Button(main,text="Log in",command=lambda: adminCheck(login.get(),password.get())).grid(row=4,column=0)


main.mainloop()