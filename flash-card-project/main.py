import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []
flip_timer = None

# ---------------------------- LOAD DATA ------------------------------- #
def load_words():
    try:
        data = pd.read_csv("data/to_learn_words.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/french_words.csv")
    return data.to_dict(orient="records")


# ---------------------------- SAVE ON EXIT ------------------------------- #
def on_closing():
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn_words.csv", index=False)
    window.destroy()


# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    if not to_learn:
        messagebox.showinfo("Congratulations!", "You've learned all the words!")
        window.destroy()
        return

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    flip_timer = window.after(flip_delay.get() * 1000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# ---------------------------- KNOWN WORD ------------------------------- #
def remove_it():
    to_learn.remove(current_card)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashy - Learn French")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.protocol("WM_DELETE_WINDOW", on_closing)

flip_delay = tk.IntVar(value=3)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 270, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=2, column=0, pady=20, padx=20)

tick_img = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_it)
known_button.grid(row=2, column=1, pady=20, padx=20)

# Flip Delay Control
delay_label = tk.Label(text="Flip Delay (s):", font=("Arial", 12), bg=BACKGROUND_COLOR)
delay_label.grid(row=3, column=0)

delay_slider = tk.Scale(from_=1, to=10, orient="horizontal", variable=flip_delay, bg=BACKGROUND_COLOR)
delay_slider.grid(row=3, column=1)

# Load data and start
to_learn = load_words()
flip_timer = window.after(flip_delay.get() * 1000, flip_card)
next_card()

window.mainloop()
