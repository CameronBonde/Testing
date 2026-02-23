import json
import os
import tkinter as tk

from dataclasses import dataclass, asdict


@dataclass
class Player:
    name: str
    xp: int
    score: int


player_stats_file = "playerStats.json"


def clear():
    name_input_field.delete(0, tk.END)
    xp_input_field.delete(0, tk.END)
    score_input_field.delete(0, tk.END)


def save():
    player.name = name_input_field.get()
    # validate user input
    try:
        player.xp = int(xp_input_field.get())
        player.score = int(score_input_field.get())
    except ValueError:
        user_message_var.set("Invalid input, integers only")
        return

    saved_text_dict = asdict(player)
    with open(player_stats_file, "w") as file:
        json.dump(saved_text_dict, file)
        user_message_var.set("Saved!")


def load():
    try:
        with open(player_stats_file, "r") as file:
            raw_json = json.load(file)

            player.name = raw_json["name"]
            player.xp = raw_json["xp"]
            player.score = raw_json["score"]

            name_input_field.delete(0, tk.END)
            name_input_field.insert(0, player.name)

            xp_input_field.delete(0, tk.END)
            xp_input_field.insert(0, str(player.xp))

            score_input_field.delete(0, tk.END)
            score_input_field.insert(0, str(player.score))

            user_message_var.set("Loaded!")
            return
    except FileNotFoundError:
        user_message_var.set("No saved json file")
    except json.decoder.JSONDecodeError:
        user_message_var.set("Invalid json file")


def delete():
    try:
        os.remove(player_stats_file)
        user_message_var.set("Deleted")
    except FileNotFoundError:
        user_message_var.set("No saved text file")


root = tk.Tk()
root.geometry("300x300")
root.title("Playerz Statz")
root.resizable(False, False)

padding = 5

# button frame
button_frame = tk.Frame()
button_frame.pack(pady=padding)

clear_button = tk.Button(button_frame, text="Clear", command=clear)
load_button = tk.Button(button_frame, text="Load", command=load)
save_button = tk.Button(button_frame, text="Save", command=save)
delete_button = tk.Button(button_frame, text="Delete", command=delete)

# grid
clear_button.grid(row=0, column=1, padx=padding)
load_button.grid(row=0, column=2, padx=padding)
save_button.grid(row=0, column=3, padx=padding)
delete_button.grid(row=0, column=4, padx=padding)

# next frame for input/output text
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=padding)

name_label = tk.Label(bottom_frame, text='Player name', font=("Arial", 12))
name_label.pack(pady=padding)
name_input_field = tk.Entry(bottom_frame, width=30, font=("Arial", 12), justify="center")
name_input_field.pack(pady=padding)

xp_label = tk.Label(bottom_frame, text='XP', font=("Arial", 12))
xp_label.pack(pady=padding)

xp_input_field = tk.Entry(bottom_frame, width=30, font=("Arial", 12), justify="center")
xp_input_field.pack(pady=padding)

score_label = tk.Label(bottom_frame, text='Score', font=("Arial", 12))
score_label.pack(pady=padding)
score_input_field = tk.Entry(bottom_frame, width=30, font=("Arial", 12), justify="center")
score_input_field.pack(pady=padding)

# user messages
user_message_var = tk.StringVar()
user_message = tk.Label(bottom_frame, textvariable=user_message_var, font=("Arial", 12))
user_message.pack(pady=padding)

player = Player(name="", xp=0, score=0)

root.mainloop()
