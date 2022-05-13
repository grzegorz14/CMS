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
                       articles text,
                       id int
                       )""")
    myCursor.execute(
        f"INSERT INTO settings (pageName,pageLayout,colorTheme,fontSize,fontFamily,menuVariant,galleryDisplay,imagesSize,links,slides,articles,id) VALUES ('CMS', 'classic', 'Light','17','Arial, Helvetica, sans-serif','1','Row','300','[]','[]','[]','1')")
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
    global delete
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


def addUser(login, password, permissions):
    jest = False
    print(login, password, permissions)
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
        jest = False
        add.destroy()


def openAddUsersPage():
    global add
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
    permissions = OptionMenu(add, variable, "user", "moderator", "admin")
    permissions.grid(row=5, column=0)
    Button(add, text="Add User", command=lambda: addUser(login.get(), password.get(), variable.get())).grid(row=0,column=1)



def adminCheck(login, password):
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


def setSetting(pageName, pageLayout, colorTheme, fontSize, fontFamily, menuVariant, galleryDisplay, imagesSize):
    sett = [pageName, pageLayout, colorTheme, fontSize, fontFamily, menuVariant, galleryDisplay, imagesSize]
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM settings")
    settings = myCursor.fetchall()
    for i,x in enumerate(sett):
        if x == '':
            print(sett[i])
            print(settings[0][i])
            sett[i] = settings[0][i]
    print(sett)

    myCursor.execute(f"UPDATE settings SET pageName = '{sett[0]}', pageLayout = '{sett[1]}', colorTheme = '{sett[2]}', fontSize = '{sett[3]}', fontFamily='{sett[4]}', menuVariant='{sett[5]}', galleryDisplay='{sett[6]}', imagesSize='{sett[7]}'")
    myConnection.commit()



def openDialog():
    main.destroy()
    dialog = Tk()
    dialog.title("Edition Page")
    dialog.geometry("420x300")
    Label(dialog, text="Users: ").grid(row=0, column=0)
    Button(dialog, text="Edit Users", command=openRoot).grid(row=0, column=1)
    Button(dialog, text="Delete Users", command=openDeleteRoot).grid(row=0, column=2)
    Button(dialog, text="Add Users", command=openAddUsersPage).grid(row=0, column=3)

    Label(dialog, text="Page Name: ").grid(row=1, column=0)
    entry1 = Entry(dialog)
    entry1.grid(row=1, column=1)

    Label(dialog, text="Page Layout: ").grid(row=2, column=0)
    variable1 = StringVar(dialog)
    variable1.set("classic")
    OptionMenu(dialog, variable1, "classic", "imageLover","newsFirst","middleSlider","gifsFan","reverse").grid(row=2, column=1)

    Label(dialog, text="Color Theme: ").grid(row=3, column=0)
    variable2 = StringVar(dialog)
    variable2.set("Light")
    OptionMenu(dialog, variable2, "Light", "Dark", "High Contrast").grid(row=3, column=1)

    Label(dialog, text="Font Size: ").grid(row=4, column=0)
    entry2 = Entry(dialog)
    entry2.grid(row=4, column=1)

    Label(dialog, text="Font Family: ").grid(row=5, column=0)
    entry3 = StringVar(dialog)
    entry3.set("Arial, Helvetica, sans-serif")
    OptionMenu(dialog, entry3,"Arial, Helvetica, sans-serif","'Courier New', Courier, monospace", "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif","'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif","'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans'").grid(row=5, column=1)

    Label(dialog, text="Menu Variant: ").grid(row=6, column=0)
    variable3 = StringVar(dialog)
    variable3.set("1")
    OptionMenu(dialog, variable3, "1", "2").grid(row=6, column=1)

    Label(dialog, text="Gallery Display: ").grid(row=7, column=0)
    variable4 = StringVar(dialog)
    variable4.set("Row")
    OptionMenu(dialog, variable4, "Row", "Column").grid(row=7, column=1)

    Label(dialog, text="Images Size: ").grid(row=8, column=0)
    entry4 = Entry(dialog)
    entry4.grid(row=8, column=1)

    Button(dialog, text="Set",
           command=lambda: setSetting(entry1.get(), variable1.get(), variable2.get(), entry2.get(), entry3.get(),
                                      variable3.get(), variable4.get(), entry4.get())).grid(row=9, column=1)


def editUserData(login, password, permissions):

    print(login)
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    for user in users:
        if user[0] == login:
            global edit
            edit = Tk()
            edit.title("Edit Page")
            edit.geometry("300x300")
            Label(edit, text="Login").grid(row=0, column=0)
            newLogin = Entry(edit)
            newLogin.insert(0, login)
            newLogin.grid(row=0, column=1)

            Label(edit, text="Password").grid(row=1, column=0)
            newPassword = Entry(edit)
            newPassword.insert(0, password)
            newPassword.grid(row=1, column=1)
            Label(edit, text="Permissions").grid(row=2, column=0)
            variable = StringVar(edit)
            variable.set(permissions)
            newPermissions = OptionMenu(edit, variable, "user", "moderator", "admin")
            newPermissions.grid(row=2, column=1)
            Button(edit, text="Zapisz",command=lambda: saveData(newLogin.get(), newPassword.get(), variable.get(), str(login))).grid(row=3,column=0)


def deleteUserData(login, password, permissions):
    # delete.destroy()
    print(login)
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()

    myCursor.execute(
        f"DELETE FROM users WHERE login = '{login}'")
    myConnection.commit()


def saveData(newLogin, newPassword, newPermissions, oldLogin):
    edit.destroy()
    myConnection = sqlite3.connect('database.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    # if newPassword == "" or newLogin == "" or newPassword.isspace() or newLogin.isspace():
    #     error = 'Some fields were empty, user is not updated.'

    myCursor.execute(
        f"UPDATE users SET login = '{newLogin}', password = '{newPassword}', permissions = '{newPermissions}' WHERE login = '{oldLogin}'")
    myConnection.commit()
    myCursor.execute("SELECT * FROM users")
    users = myCursor.fetchall()
    myConnection.close()
    print(users)
    info = 'User is updated'


Label(main, text="Login").grid(row=0, column=0)
login = Entry(main)
login.grid(row=1, column=0)
Label(main, text="Password").grid(row=2, column=0)
password = Entry(main)
password.grid(row=3, column=0)
Button(main, text="Log in", command=lambda: adminCheck(login.get(), password.get())).grid(row=4, column=0)

main.mainloop()