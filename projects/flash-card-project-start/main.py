BG_COLOR = "#B1DDC6"
FONT = "Arial"

import pandas
from tkinter import *
import random

r_or_w = 0
timer = None

data = pandas.read_csv("data/french_words.csv")
french_dict = {row.English:row.French for (index,row) in data.iterrows()}

screen = Tk()
screen.minsize(width=900,height=800)
screen.config(bg=BG_COLOR, padx=10, pady=10)

back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")
check = PhotoImage(file="images/right.png")
x = PhotoImage(file="images/wrong.png")

fc_front_cv = Canvas(width=800,height=526,bg=BG_COLOR,highlightthickness=0)
fc_back_cv = Canvas(width=800,height=526,bg=BG_COLOR,highlightthickness=0)
fc_front_cv.create_image(400,270,image=front)
fc_back_cv.create_image(400, 270, image=back)
fc_front_cv.create_text(400,170,text="English",font=(FONT,30,"italic"),fill="black")
fc_back_cv.create_text(400, 170, text="French", font=(FONT, 30, "italic"), fill="white")
text_front = fc_front_cv.create_text(400,270,text="",font=(FONT,50,"bold"),fill="black")
text_back = fc_back_cv.create_text(400,270,text="",font=(FONT,50,"bold"),fill="black")

def flash_card(count, english, french):
    fc_front_cv.grid(column=0,row=0,columnspan=2, pady=50, padx=40)
    fc_front_cv.itemconfig(text_front, text=f"{english}")
    if count > 0:
        global timer
        timer = screen.after(1000,flash_card, count - 1, english, french)
    else:
        fc_back_cv.grid(column=0, row=0, columnspan=2, pady=50, padx=40)
        fc_back_cv.itemconfig(text_back, text=f"{french}")

english, french = random.choice(list(french_dict.items()))
flash_card(5, english, french)

def wrong_cmd():
    global r_or_w
    r_or_w = 0
    button_cmd()

def right_cmd():
    global r_or_w
    r_or_w = 1
    button_cmd()

def button_cmd():
    global timer
    global r_or_w
    screen.after_cancel(timer)

    english, french = random.choice(list(french_dict.items()))
    fc_front_cv.itemconfig(text_front, text=f"")
    fc_back_cv.itemconfig(text_back, text=f"")
    if fc_back_cv.winfo_ismapped():
        fc_back_cv.grid_forget()
    flash_card(5, english, french)
    if r_or_w == 1:
        french_dict.pop(english)

button_check = Button(height=100,width=100)
button_check.config(image=check, highlightthickness=0, command=right_cmd)
button_check.config(borderwidth=0, relief="flat")
button_check.grid(column=1,row=1)

button_x = Button(height=99,width=100)
button_x.config(image=x, highlightthickness=0, command=wrong_cmd)
button_x.config(borderwidth=0, relief="flat")
button_x.grid(column=0,row=1)

screen.mainloop()