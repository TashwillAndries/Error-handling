# Tashwill Andries

# importing tkinter

from tkinter import *
from tkinter import messagebox

# setting up the window
login = Tk()
login.geometry("300x200")
login.config(bg="light grey")
login.title("Authorization")

# the tkinter layout
heading = Label(login, text="Please enter login details")
heading.pack()
name_label = Label(login, text="Username", bg="light grey")
name_label.pack()
name_entry = Entry(login)
name_entry.pack()
password_label = Label(login, text="Password", bg="light grey")
password_label.pack()
password_entry = Entry(login)
password_entry.pack()


# function to get the passwords and usernames
def log():
    username = {"Tashwill": "2521", "Zaid": "3682", "Nathan": "8954", "Mujaid": "4640", "Mikayla": "9998"}

    if username.get(name_entry.get()):
        if username[name_entry.get()] == password_entry.get():
            messagebox.showinfo("Message", "Access Granted")
            login.destroy()
            import newscreen
        else:
            messagebox.showerror("Message", "Access Denied")


login_btn = Button(login, text="Login", bg="purple", command=log)
login_btn.pack()
login.mainloop()
