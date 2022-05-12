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
                       pageName text,
                       pageLayout text,
                       colorTheme text,
                       fontSize int,
                       fontFamily text,
                       menuVariant text,
                       galleryDisplay text,
                       imagesSize int,
                       links text,
                       slides text,
                       articles text
                       )""")
    myCursor.execute(f"INSERT INTO settings (pageName,pageLayout,colorTheme,fontSize,fontFamily,menuVariant,galleryDisplay,imagesSize,links,slides,articles) VALUES ('CMS', 'classic', 'Light','17','Arial, Helvetica, sans-serif','1','Row','300','','','')")
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
def setSetting(settingType,change):

    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM settings")
    print(settingType)
    print(change)
    myCursor.execute(f"UPDATE settings SET {settingType} = '{change}'")
    settings = myCursor.fetchall()
    print(settings)
    

def openDialog():
    dialog = Tk()
    dialog.title("Edition Page")
    dialog.geometry("300x300")
    Label(dialog, text="Users: ").grid(row=0, column=0)
    Button(dialog, text="Edit Users", command=openRoot).grid(row=0, column=1)
    Button(dialog, text="Delete Users", command=openDeleteRoot).grid(row=0, column=2)
    Button(dialog, text="Add Users", command=openAddUsersPage).grid(row=0, column=3)

    Label(dialog, text="Page Name: ").grid(row=1, column=0)
    entry1 = Entry(dialog)
    entry1.grid(row=1, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("pageName",entry1.get())).grid(row=1, column=2)

    Label(dialog, text="Page Layout: ").grid(row=2, column=0)
    variable1 = StringVar(dialog)
    variable1.set("classic")
    OptionMenu(dialog, variable1, "classic", "2").grid(row=2, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("pageLayout",variable1.get())).grid(row=2, column=2)

    Label(dialog, text="Color Theme: ").grid(row=3, column=0)
    variable2 = StringVar(dialog)
    variable2.set("Light")
    OptionMenu(dialog, variable2, "Light", "Dark", "High Contrast").grid(row=3, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("colorTheme",variable2.get())).grid(row=3, column=2)

    Label(dialog, text="Font Size: ").grid(row=4, column=0)
    entry2 = Entry(dialog)
    entry2.grid(row=4, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("fontSize",entry2.get())).grid(row=4, column=2)

    Label(dialog, text="Font Family: ").grid(row=5, column=0)
    entry3 = Entry(dialog)
    entry3.grid(row=5, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("fontFamily",entry3.get())).grid(row=5, column=2)

    Label(dialog, text="Menu Variant: ").grid(row=6, column=0)
    variable3 = StringVar(dialog)
    variable3.set("1")
    OptionMenu(dialog, variable3, "1", "2").grid(row=6, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("menuVariant",variable3.get())).grid(row=6, column=2)

    Label(dialog, text="Gallery Display: ").grid(row=7, column=0)
    variable4 = StringVar(dialog)
    variable4.set("Row")
    OptionMenu(dialog, variable4, "Row", "2").grid(row=7, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("galleryDisplay",variable4.get())).grid(row=7, column=2)

    Label(dialog, text="Images Size: ").grid(row=8, column=0)
    entry4 = Entry(dialog)
    entry4.grid(row=8, column=1)
    Button(dialog, text="Set", command= lambda:setSetting("imagesSize",entry4.get())).grid(row=8, column=2)


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