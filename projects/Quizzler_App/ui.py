THEME_COLOR = "#375362"
FONT = ("Arial",20,"normal")
from tkinter import *
from quiz_brain import QuizBrain

class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.minsize(height=500,width=300)
        self.screen.config(pady=10,padx=30,bg=THEME_COLOR)
        self.score_txt = Label(text = "Score: 0",fg="white",bg=THEME_COLOR,font=FONT)
        self.score_txt.config(pady=20)
        self.score_txt.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.text_in = self.canvas.create_text(150, 100,fill=THEME_COLOR,font= ("Arial",20,"italic"), width=200)
        self.canvas.itemconfig(self.text_in,text="This is a dummy text bruh lets test it")
        self.canvas.grid(column=0, row=1,columnspan= 2)

        self.photo_true = PhotoImage(file="images/true.png")
        self.photo_false = PhotoImage(file="images/false.png")

        self.yes_btn = Button(height=97,width=100)
        self.yes_btn.config(image=self.photo_true,highlightthickness=0,command=self.true_cmd)
        self.yes_btn.grid(column=0,row=2, pady=30)

        self.no_btn = Button(height=97, width=100)
        self.no_btn.config(image=self.photo_false,highlightthickness=0,command=self.false_cmd)
        self.no_btn.grid(column=1, row=2, pady=30)

        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.text_in, text=q_text)

    def end_screen(self):
        self.canvas.itemconfig(self.text_in, text="You've completed the Quizzler!\n" +
                                                  f"Your final score is: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.canvas.itemconfig(self.text_in,fill="#FFCF92", font=("Arial",25,"bold"), anchor="center")
        self.canvas.config(bg="#8296A1")

    def set_white(self):
        self.canvas.config(bg="white")
        self.get_next_question()

    def check_true_false(self, val):
        if self.quiz_brain.still_has_questions():
            if self.quiz_brain.check_answer(val):
                self.canvas.config(bg="#239E5A")
                self.screen.after(1000,self.set_white)
            else:
                self.canvas.config(bg="#FF4B3B")
                self.screen.after(1000, self.set_white)
            self.score_txt.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.end_screen()
        self.quiz_brain.question_number += 1

    def true_cmd(self):
        self.check_true_false("true")

    def false_cmd(self):
        self.check_true_false("false")




