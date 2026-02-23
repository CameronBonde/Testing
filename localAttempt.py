import json
from tkinter import *

def clear():
    player_name.set("")
    xp.set(0)
    score.set(0)
    status_label.config(text="")

def load():
    try:
        with open("player_data.json", "r") as f:
            data = json.load(f)
            player_name.set(data["name"])
            xp.set(data["xp"])
            score.set(data["score"])
        status_label.config(text="Loaded!")
    except FileNotFoundError:
        clear()
        status_label.config(text="")

def save():
    data = {
        "name": player_name.get(),
        "xp": xp.get(),
        "score": score.get()
    }
    with open("player_data.json", "w") as f:
        json.dump(data, f)
    status_label.config(text="Saved!")

def delete():
    with open("player_data.json", "w") as f:
        json.dump({}, f)  # Clear file
    clear()
    status_label.config(text="Deleted!")

root = Tk()
root.title("Playerz Statz")

# Frame for buttons
button_frame = Frame(root)
clear_btn = Button(button_frame, text="Clear", command=clear)
load_btn = Button(button_frame, text="Load", command=load)
save_btn = Button(button_frame, text="Save", command=save)
delete_btn = Button(button_frame, text="Delete", command=delete)

# Arrange buttons in grid
clear_btn.grid(row=0, column=0, padx=2)
load_btn.grid(row=0, column=1, padx=2)
save_btn.grid(row=0, column=2, padx=2)
delete_btn.grid(row=0, column=3, padx=2)

button_frame.pack(side="top", pady=(5, 0))

# Frame for content (labels/entries/status)
content_frame = Frame(root)
content_frame.pack(side="top", pady=(10, 5))

# Player name
Label(content_frame, text="Player name").grid(row=0, column=0, sticky=W, pady=2)
player_entry = Entry(content_frame)
player_entry.grid(row=0, column=1, pady=2)
player_name = StringVar(value="Cam")
player_entry.config(textvariable=player_name)

# XP
Label(content_frame, text="XP").grid(row=1, column=0, sticky=W, pady=2)
xp_entry = Entry(content_frame)
xp_entry.grid(row=1, column=1, pady=2)
xp = IntVar(value=30)
xp_entry.config(textvariable=xp)

# Score
Label(content_frame, text="Score").grid(row=2, column=0, sticky=W, pady=2)
score_entry = Entry(content_frame)
score_entry.grid(row=2, column=1, pady=2)
score = IntVar(value=42)
score_entry.config(textvariable=score)

# Status label
status_label = Label(content_frame, text="")
status_label.grid(row=3, column=0, columnspan=2)  # Span both columns

root.mainloop()
