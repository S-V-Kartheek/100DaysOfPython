from tkinter import *
from quiz_brain import Quiz_brain

THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self,quiz_brain:Quiz_brain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        score=0
        self.score_label=Label(text=f"score: {score}",fg="white",bg=THEME_COLOR,font=("Courier",15,"bold"))
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250)
        self.question_text=self.canvas.create_text(150,125,width=280,text="Some text here",fill=THEME_COLOR,font=("Arial",15,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=40)



        tick=PhotoImage(file="images/right.png")
        self.true_button=Button(image=tick,highlightthickness=0,command=self.TruePressed)
        self.true_button.grid(row=2,column=0)

        wrong = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0,command=self.FalsePressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_have_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_txt=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_txt)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached end of the quiz")
            self.close_button=Button(text="close",command=self.close)
            self.close_button.grid(row=2,column=0,columnspan=2)
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def TruePressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def FalsePressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="light green")
        else:
            self.canvas.config(bg="orange")
        self.window.after(1000,self.get_next_question)

    def close(self):
        self.window.destroy()