from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import pyperclip        #used for copy/paste clipboard functions
import datetime
import time

FONT = ("Arial", 10, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)

    password_input.delete(0,END)
    password_input.insert(0,str(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    keys = ["website", "username", "password"]

    if website_input.get() == "" or website_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Listen Up", message="no empty fields allowed")

    else:

        value_entry = [website_input.get(), username_input.get(), password_input.get()]
        entry_dict = {key: value for (key, value) in zip(keys, value_entry)}

        if messagebox.askyesno(title="please Confirm", message=f"{entry_dict}\n it this okay?"):
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

            with open("data.txt", "a") as data_file:
                data_file.write(f"{str(entry_dict)},\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# the canvas
canvas = Canvas(width=150, height=110)
mypass_img = PhotoImage(file=r"C:\Users\akshun chauhan\Desktop\semester 1\python final project\akshun\Password Vault\akshun_000363152_final\New folder\logo4.png")

#mypass_img = PhotoImage(file="logo4.png")
canvas.create_image(40, 60, image=mypass_img)
canvas.grid(row=0, column=1)

# website: label
website = Label(text="Website: ", font=FONT)
website.grid(row=1, column=0)

# email/username label
username = Label(text="Email/Username: ", font=FONT)
username.grid(row=2, column=0)

# password: label
password = Label(text="Password: ", font=FONT)
password.grid(row=3, column=0)

# website_input box
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# username_input box
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

# password_input box
#password_input = Entry(width=35,show="*")
password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# generate password button
gen_pass = Button(text="Generate password", command=generate_password)
gen_pass.grid(row=4, column=1)

# Add button
add_button = Button(text="Add", command=add)
add_button.grid(row=4, column=2)

window.mainloop()