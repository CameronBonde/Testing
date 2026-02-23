import os
import tkinter as tk

def clicked():
    input_field.insert(tk.END, "BUM!")

def clear():
    input_field.delete(0, tk.END)

def save():
    saved_text = input_field.get()
    with open("saved_text.txt", "w") as file:
        file.write(saved_text)
        user_message_var.set("Saved!")

def load():
    loaded_text = ""
    try:
        with open("saved_text.txt", "r") as file:
            loaded_text = file.read()
            input_field.delete(0, tk.END)
            input_field.insert(0, loaded_text)
            user_message_var.set("Loaded!")
            return loaded_text
    except FileNotFoundError:
        user_message_var.set("No saved text file")

def delete():
    try:
        os.remove("saved_text.txt")
        user_message_var.set("Deleted")
    except FileNotFoundError:
        user_message_var.set("No saved text file")

root = tk.Tk()
root.geometry("300x300")
root.title("Cam rules!")
root.resizable(False, False)

padding = 5

# button frame
button_frame = tk.Frame()
button_frame.pack(pady=padding)

add_great_ideas_button = tk.Button(button_frame, text="Press me", command=clicked)
clear_button = tk.Button(button_frame, text="Clear", command=clear)
load_button = tk.Button(button_frame, text="Load", command=load)
save_button = tk.Button(button_frame, text="Save", command=save)
delete_button = tk.Button(button_frame, text="Delete", command=delete)

# grid
add_great_ideas_button.grid(row=0, column=0, padx=padding)
clear_button.grid(row=0, column=1, padx=padding)
load_button.grid(row=0, column=2, padx=padding)
save_button.grid(row=0, column=3, padx=padding)
delete_button.grid(row=0, column=4, padx=padding)

# next frame for input/output text
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=padding)

input_field = tk.Entry(bottom_frame, width=30, font=("Arial", 12), justify="center")
input_field.pack(pady=padding)

# user messages
user_message_var = tk.StringVar()
user_message = tk.Label(bottom_frame, textvariable=user_message_var, font=("Arial", 22))
user_message.pack(pady=padding)

root.mainloop()
