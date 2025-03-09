from tkinter import *

window = Tk()
window.title("My Program")
window.minsize(width=500,height=600)


# label
my_label = Label(text="I am a label", font=("Lato",24,"normal"))
my_label.pack()
my_label.config(text="I understand it now")

enter_name = Label(text="Enter your name")
enter_name.pack()


# Entry
my_input = Entry(width=10)
my_input.pack()

# button

def button_action():
    name = my_input.get()
    #gets current value in textbox at line 1, character 0
    print(my_text.get("1.0",END))
    my_label.config(text=f"Click my child {name}")
    new_label = Label(text="I am clicked")
    new_label.pack()

my_button = Button(text="click click", command=button_action)
my_button.pack()

# text
my_text = Text(width=20, height=10)
my_text.focus()
my_text.insert(END,"Put text here")
my_text.pack()

#spinbox
def spinbox_used():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0,to=5,width=3,command=spinbox_used)
my_spinbox.pack()

#scale
def scale_used(value):
    print(value)
my_scale = Scale(from_=0,to=50,command=scale_used)
my_scale.pack()

#checkbox
def check_button():
    print(checked.get())

checked = IntVar()
check_button = Checkbutton(text="on or no?",variable=checked,command=check_button)
checked.get()
check_button.pack()

#radio_button
def radio_cmd():
    print(radio_state.get())
radio_state = IntVar()
radio_btn_1 = Radiobutton(text="Option 1",value=1, variable=radio_state,command=radio_cmd)
radio_btn_2 = Radiobutton(text="Option 2",value=2, variable=radio_state,command=radio_cmd)
radio_btn_1.pack()
radio_btn_2.pack()

#listbox
def listbox_func(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(width=10, height=3)
fruits = ["apple", "orange", "mango"]
for s in fruits:
    listbox.insert(fruits.index(s),s)
listbox.bind("<<ListboxSelect>>", listbox_func)
listbox.pack()

window.mainloop()








# Unlimited positional Args *args && Keyword Arguments **kwargs

# def my_func(*args, **kwargs):
#     res = 0
#     for n in args:
#         res += n
#     for key, val in kwargs.items():
#         if key == "mult":
#             res *= val
#         elif key == "divide":
#             res /= val
#     return res
# test = my_func(123,312,123,123, mult = 69, divide = 2)
# print(test)

# Using Class

# class Car:
#     def __init__(self, **kw):
#         self.info = kw
#
#     def info_print(self):
#         for key,val in self.info.items():
#             print(f"{key}->{val}")
#
# car_one = Car(brand="Mazda", color="red", year=2006)
# car_one.info_print()
