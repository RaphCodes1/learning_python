from tkinter import *

def miles_to_km():
    val = round(int(entry1.get()) * 0.621371, 2)
    res.config(text=str(val))

screen = Tk()
screen.minsize(width=300,height=100)
screen.config(padx=40,pady=20)
screen.title("KM to miles Converter")

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

entry1 = Entry(width=5)
entry1.grid(column=1,row=0)

res = Label(text="0")
res.grid(column=1,row=1)

my_btn = Button(text="Calculate", command=miles_to_km)
my_btn.grid(column=1,row=2)

miles_txt = Label(text="Miles")
miles_txt.grid(column=2, row=1)

km_txt = Label(text="Km")
km_txt.grid(column=2, row=0)

screen.mainloop()