import tkinter as tk
from random import shuffle

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("\u0e02", "Khor Khai (ขอ ไข่)"),
    ("\u0e04", "Kor Kwai (คอ ควาย)"),
    ("\u0e06", "Khor Rakhang (ฆอ ระคัง)"),
    ("\u0e08", "Jor Jaan (จอ จาน)")
]

shuffle(thai_consonants)
current_index = 0
flipped = False

def flip_card():
    global flipped
    flipped = not flipped
    update_card()

def next_card():
    global current_index, flipped
    if current_index < len(thai_consonants) - 1:
        current_index += 1
    flipped = False
    update_card()

def prev_card():
    global current_index, flipped
    if current_index > 0:
        current_index -= 1
    flipped = False
    update_card()

def update_card():
    character, name = thai_consonants[current_index]
    if flipped:
        canvas.itemconfig(card_text, text=name, font=("Arial", 20))
    else:
        canvas.itemconfig(card_text, text=character, font=("Arial", 50))

# Setup Tkinter window
root = tk.Tk()
root.title("Thai Consonant Flashcards")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

card_text = canvas.create_text(150, 100, text="", font=("Arial", 50))
update_card()

# Buttons
flip_button = tk.Button(root, text="Flip", command=flip_card)
flip_button.pack(side=tk.LEFT, padx=10)

prev_button = tk.Button(root, text="Previous", command=prev_card)
prev_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(root, text="Next", command=next_card)
next_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
