from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_SMALL = ("Alegreya", 40, "italic")
FONT_LARGE = ("Alegreya", 60, "bold")
current_card = {}
to_learn = {}

# Read Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """Show next card"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_card["French"], fill="black")
    card.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    """Remove card from list, save new words_to_learn list, show next card"""
    to_learn.remove(current_card)
    new_csv = pandas.DataFrame(to_learn)
    new_csv.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    """Show card back"""
    global current_card
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")
    card.itemconfig(card_background, image=card_back_image)


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card
card = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = card.create_image(400, 263, image=card_front_image)
card_title = card.create_text(400, 150, text="", font=FONT_SMALL)
card_word = card.create_text(400, 263, text="", font=FONT_LARGE)
card.grid(column=0, row=0, columnspan=2)
card.config()

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                      command=next_card)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()