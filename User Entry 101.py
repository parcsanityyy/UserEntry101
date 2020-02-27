import tkinter as tk
from tkinter import messagebox
import os


login = tk.Tk()
login.eval("tk::PlaceWindow . Center")
login.title("Login")
#login.iconbitmap('C:\\Python\\gp.ico')
login.resizable(False, False)
login.geometry('230x80')

usernamevar  = tk.StringVar()
passwordvar = tk.StringVar()

newusernamevar = tk.StringVar()
newpasswordvar = tk.StringVar()
newcnfrmpasswordvar = tk.StringVar()
newemailvar = tk.StringVar()

userfile = 'C:\\Desktop\\Python\\users.txt'

try:
    if not os.path.exists(userfile):
        open(userfile, 'w+')
except Exception as e:
    raise e


def validateLogin():  
    username = usernamevar.get()
    password = passwordvar.get()
    contents = open(userfile)
    userpasslist = contents.readline()
    userpass = username + ":" + password
    print(userpass)
    if userpass not in userpasslist:
        messagebox.showinfo('Warning','Incorrect username/password.')
        return
    if password == '':
        messagebox.showinfo('Warning','Please enter your password.')
        return
    if userpass in userpasslist:
        messagebox.showinfo("Login Success", "Welcome!")
        return

def validateSignup():
    username = newusernamevar.get()
    password = newpasswordvar.get()
    cnfrmpassword = newcnfrmpasswordvar.get()
    email = newemailvar.get()

    print(username)
           
    contents = open(userfile)
    userpasslist = contents.readline()
    userpass = username + ":" + password

    if userpass in userpasslist:
        messagebox.showinfo('Warning','User name already taken.')
        return
    if not password == cnfrmpassword:
        messagebox.showinfo('Warning','Passwords mismatch.')
        return
    if password == "":
        messagebox.showinfo('Warning','Please enter a password.')
        return
    if cnfrmpassword == "":
        messagebox.showinfo('Warning','Please confirm your password.')
        return

    createNewUser()
    return
    #registerForm.destroy()
    

def createNewUser():

    username = newusernamevar.get()
    password = newpasswordvar.get()
    cnfrmpassword = newcnfrmpasswordvar.get()
    email = newemailvar.get()

    addNewuser = open(userfile, 'a')
    addNewuser.write(username + ":" + password + "\n")

    newusernamevar.set('')
    newpasswordvar.set('')
    newcnfrmpasswordvar.set('')
    newemailvar.set('')

#REGISTER FORM#
def createAccount():
    #login.destroy()
    registerForm = tk.Toplevel(login)
    #registerForm.eval('tk::PlaceWindow . Center')
    registerForm.title('Create a New Account')
    registerForm.resizable(False, False)
    registerForm.geometry('230x115')

    newUsernameLabel = tk.Label(registerForm, text = 'Username', justify = 'left', anchor = 'w').grid(row = 0, column = 0)
    newPasswordLabel = tk.Label(registerForm, text = 'Password', justify = 'left', anchor = 'w').grid(row = 1, column = 0)
    newCnfrmPasswordLabel = tk.Label(registerForm, text = 'Confirm Password', justify = 'left', anchor = 'w').grid(row = 2, column = 0)
    newEmailLabel = tk.Label(registerForm, text = 'Email Address', justify = 'left', anchor = 'w').grid(row = 3, column = 0)

    newUsernameEntry = tk.Entry(registerForm, textvariable = newusernamevar).grid(row = 0, column = 1)
    newPasswordEntry = tk.Entry(registerForm, textvariable = newpasswordvar).grid(row = 1, column = 1)
    newCnfrmPasswordEntry = tk.Entry(registerForm, textvariable = newcnfrmpasswordvar).grid(row = 2, column = 1)
    newEmailEntry = tk.Entry(registerForm, textvariable = newemailvar).grid(row = 3, column = 1)

    newcreateAccountButton = tk.Button(registerForm, text = 'Sign up', command = validateSignup).grid(row = 4, column = 1)


    registerForm.mainloop()
#END OF REGISTER FORM#


#LOGIN FORM#
usernameLabel = tk.Label(login, text = 'Username', pady = 3, justify = 'left').grid(row = 0, column = 0)
passwordLabel = tk.Label(login, text = 'Password', pady = 3, justify = 'left').grid(row = 1, column = 0)

usernameEntry = tk.Entry(login, textvariable = usernamevar).grid(row = 0 ,column = 1)
passwordEntry = tk.Entry(login, textvariable = passwordvar).grid(row = 1, column = 1)

loginButton = tk.Button(login, text = 'Login', padx = 10, command = validateLogin).grid(row = 2, column = 1)
createAccountButton = tk.Button(login, text = 'Create Account', padx = 2, command = createAccount).grid(row = 2, column = 0)
#END OF LOGIN FORM#


login.mainloop()
