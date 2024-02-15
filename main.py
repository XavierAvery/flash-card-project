from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
BLACK = "#000000"
FONT40 = ("Ariel", 40, "italic")
FONT60 = ("Ariel", 60, "bold")
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    # Read data from french_word.cvs with pandas and generate a Dataframe
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # list the rows


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(title, text="French", fill=BLACK)
    # Read data from french_word.cvs with pandas and generate a Dataframe

    current_card = random.choice(to_learn)
    canvas.itemconfig(word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill=WHITE)
    canvas.itemconfig(word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# --------- Canvas --------- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# --------- Canvas Text  --------- #
title = canvas.create_text(400, 150, text="", font=FONT40, fill=BLACK)
word = canvas.create_text(400, 263, text="", font=FONT60, fill=BLACK)
canvas.grid(column=0, row=0, columnspan=2)

# --------- Buttons --------- #
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
