from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

FONT = ("Arial",12,"normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','(',')','*','+']

def random_pass_cmd():
    user_input = [random.randint(8,10), random.randint(2,4),
                  random.randint(2,4)]
    values_for_pass = {"letters":letters,
                       "symbols":symbols,
                       "numbers":numbers}
    pass_sorted = []
    for index, key in zip(user_input,values_for_pass):
        for _ in range(int(index)):
            pass_sorted.append(random.choice(values_for_pass[key]))
    random.shuffle(pass_sorted)
    pass_str = "".join(pass_sorted)
    entry_password.insert(0,pass_str)
    pyperclip.copy(pass_str)

# ---------------------------- SEARCH COMMAND ------------------------------- #

def search_cmd():
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message=f"Enter Data first.")
    else:
            input_search = entry_website.get()
            present = 0
            info = []
            for key in data:
                if input_search == key:
                    present = 1
                    for one, data in data[key].items():
                        info.append(f"{one}: {data}")
            if present:
                msg = '\n'.join(info)
                messagebox.showinfo("Items",msg)
            else:
                messagebox.showinfo("Error", "Website not found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_cmd():

    website = entry_website.get()
    email_user = entry_email_user.get()
    password = entry_password.get()
    items = {
        website: {
             "Email/User":email_user,
             "Password":password,
            }
    }
    check = messagebox.askokcancel(title="Check", message= f"Is the info correct?"
              f"Website: {website}\n"
              f"Email/Username: {email_user}\n"
              f"Password: {password}\n")
    if check:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(items, file, indent=4)
        else:
            data.update(items)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0,END)
            entry_email_user.delete(0,END)
            entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.minsize(width=500,height=300)
screen.config(bg="white",padx=30,pady=50)

logo_img = PhotoImage(file="logo.png")
picture_logo = Canvas(width=200, height=189, bg="white",highlightthickness=0)
picture_logo.create_image(74,89, image=logo_img)
picture_logo.grid(column=1,row=0)

text_one = Label(text="Website:",font=FONT,bg="white",fg="black")
text_one.config(padx=20)
text_one.grid(column=0,row=1)

text_two = Label(text="Email/Username:",font=FONT,bg="white",fg="black")
text_two.grid(column=0,row=2)

text_three = Label(text="Password:",font=FONT,bg="white",fg="black")
text_three.grid(column=0,row=3)

entry_website = Entry(width=25,font=FONT,bg="white",highlightthickness=1.1)
entry_website.config(bg="white",
                highlightbackground="#DBDCF0", highlightcolor="#DBDCF0",
                    fg="black",relief="flat",cursor="xterm")
entry_website.config(cursor="xterm",insertbackground="black")
entry_website.grid(column=1,row=1, pady=5, padx=3, sticky='w')

entry_email_user = Entry(width=41,font=FONT,highlightthickness=1.1)
entry_email_user.config(bg="white",
                highlightbackground="#DBDCF0", highlightcolor="#DBDCF0",
                    fg="black",relief="flat",cursor="xterm")
entry_email_user.config(cursor="xterm",insertbackground="black")
entry_email_user.grid(column=1,row=2, pady=5)

entry_password = Entry(width=20,font=FONT,bg="white",highlightthickness=1.1)
entry_password.config(bg="white",
                highlightbackground="#DBDCF0", highlightcolor="#DBDCF0",
                    fg="black",relief="flat")
entry_password.config(cursor="xterm",insertbackground="black")
entry_password.grid(column=1,row=3, sticky='w', pady=5, padx=3)

button_search = Button(text="Search",width=8,font="FONT",bg="white",command=search_cmd)
button_search.config(highlightbackground="white",relief="flat")
button_search.grid(column=1,row=1, sticky='e',pady=5)

button_pass = Button(text="Generate Password",width=16,font=FONT,bg="white",command=random_pass_cmd)
button_pass.config(highlightbackground="white",relief="flat")
button_pass.grid(column=1,row=3, sticky='e', pady=5)

button_add = Button(text="Add",width=38,font=FONT,bg="white")
button_add.config(bg="white",highlightbackground="white",relief="flat",command=add_cmd)
button_add.grid(column=1,row=4, pady=5)


screen.mainloop()