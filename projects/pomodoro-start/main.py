from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    screen.after_cancel(timer)
    reps = 0
    up_text.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="0:00")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_func():
    global reps
    twentyfive = 25 * 60
    five = 5 * 60
    twenty = 20 * 60
    reps += 1
    if (reps % 2 or reps == 1)and reps != 8:
        timer_func(twentyfive)
        up_text.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        timer_func(five)
        up_text.config(text="Break", fg=PINK)
    elif reps == 8:
        timer_func(twenty)
        up_text.config(text="Rest",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time

def timer_func(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count % 60}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000,timer_func,count - 1)
    else:
        if reps == 8:
            reset_timer()
        else:
            start_func()
            marks = ""
            sessions = math.floor(reps/2)
            for _ in range(sessions):
                marks += CHECK
                checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100,pady=50,bg=YELLOW)


#timer text
up_text = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"normal"))
up_text.grid(column=1,row=0)

#Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)


#buttons
start_button = Button(text="start",width=5,height=2,bd=0,command=start_func)
start_button.config(bg=YELLOW,highlightbackground="white",relief="flat")
start_button.grid(column=0,row=2)

exit_button = Button(text="reset",width=5,height=2,bd=0, command=reset_timer)
exit_button.config(bg=YELLOW,highlightbackground="white",relief="flat")
exit_button.grid(column=2,row=2)

#checkmark
checkmark = Label(fg=GREEN,font=(FONT_NAME,30,"normal"))
checkmark.config(bg=YELLOW)
checkmark.grid(column=1,row=3)

screen.mainloop()
