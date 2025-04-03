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
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_function():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)  # Reset color
    canvas.itemconfig(clock, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:   # Every 8th session → Long break
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # Even sessions → Short break
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes=math.floor(count//60)
    second=count%60
    if second<10:
        second=f"0{second}"
    canvas.itemconfig(clock,text=f"{minutes}:{second}")

    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)

canvas=Canvas(width=220,height=240,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(110,120,image=tomato_img)

clock=canvas.create_text(110,140,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)



start_button=Button(text="Start",highlightthickness=0,command =start_timer)
start_button.grid(row=2,column=0)

start_reset=Button(text="Reset",highlightthickness=0,command=reset_function)
start_reset.grid(row=2,column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"), padx=10, pady=5)
check_marks.grid(row=2,column=1)
window.mainloop()