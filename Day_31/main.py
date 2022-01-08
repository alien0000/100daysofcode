
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")

def next_card():
   current_data=random.choice(to_learn)
   canvas.itemconfig(card_title,text="French")
   canvas.itemconfig(card_word,text=current_data["French"])

def flip_card():
   canvas.itemconfig(card_title,text="English")
   canvas.itemconfig(card_word,)
window=Tk()
window.title("Flashy")

window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526)
card_back_img=PhotoImage(file="images/card_back.png")
card_front_img=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

canvas.grid(row=0,column=0,columnspan=2)

# BUTTONS
wrong_button_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_button_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_button_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_button_img,highlightthickness=0,command=next_card)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()
