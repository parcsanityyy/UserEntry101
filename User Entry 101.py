#!/usr/bin/env python
# coding: utf-8

# In[92]:


import tkinter as tk

login = tk.Tk()
    
class loginForm():
    def __init__(self):
        login.title("User Log In")

        userNameLabel = tk.Label(login, text="User Name :", width = 10, anchor = "w", justify = "left").grid(row = 0)
        userName = tk.Entry(login).grid(row = 0, column = 1)

        pwdLabel = tk.Label(login, text="Password    :", width = 10, anchor = "w", justify = "left").grid(row = 1)
        pwd = tk.Entry(login).grid(row = 1 , column = 1)

        crtAcctButton = tk.Button(login, text = "Create Account", command = signUp.signUpForm).grid(row = 3, column = 0, pady =5)
        loginButton = tk.Button(login, text="Log In", padx = 10).grid(row = 3, column =1, pady=4)
        exitButton = tk.Button(login, text="Exit", padx = 10, command = loginForm.exit).grid(row = 3, column = 2)
        
        login.mainloop()
        
    def exit():
        login.destroy()

class signUp():
    
    def signUpForm():

        a = tk.StringVar()
        b = tk.StringVar()
        loginForm.exit()
        signup = tk.Tk()
        signup.geometry('300x100')
        usernameLabel = tk.Label(signup, text = "User Name:", padx = 10).grid(row = 0)
        usernameEntry = tk.Entry(signup).grid(row = 0, column = 1)
        
        pwdLabel = tk.Label(signup, text = "Password:", padx = 10).grid(row = 1)
        pwdEntry = tk.Entry(signup).grid(row = 1, column = 1)
       
        cnfrmpwdLabel = tk.Label(signup, text = "Confirm Password:", padx = 10).grid(row = 2)
        cnfrmpwdEntry = tk.Entry(signup).grid(row = 2, column = 1)        
        
        createAcctButton = tk.Button(signup, text = "Create", command = signUp.validateSignup).grid(row = 3, column = 1)
        
    def validateSignup():
        if a == b:
            messagebox.showinfo("Sign Up", "User account has been created")                            
        
start = loginForm()

