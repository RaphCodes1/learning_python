from tkinter import *

screen = Tk()
screen.title("Playground")
screen.minsize(width=500,height=500)
screen.config(padx=100, pady=200)
my_label = Label(text="Welcome to playground")
my_label.grid(column = 0, row = 0)

my_in = Entry(width=10)
my_in.grid(column = 3, row = 2)

def btn_cmd():
    val = my_in.get()
    print(val)
my_btn = Button(text="click click",command=btn_cmd)
my_btn.grid(column = 1, row = 1)

my_btn_2 = Button(text="clack clack",command=btn_cmd)
my_btn_2.grid(column = 2, row = 0)


screen.mainloop()