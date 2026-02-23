import tkinter as tk

player_names = ["Cam", "Daveo", "Johno", "Shaz"]

def player_name_save():
    with open("player_names.txt", "w") as file:
        for counter, name in enumerate(player_names):
            file.write(player_names[counter])


# TODO
# Put the open code inside a function
# Call the function
# Make a save function
# Alter the open line above. Change the "w" to a "r" for read (w is write)
# After the file is open, read the contents.
# Type "file. " and in a real editor after the dot, it'll display a list of variables and function that are INSIDE

rootUI = tk.Tk()
rootUI.title("User Name")
rootUI.geometry("700x700")
rootUI.resizable(width=0, height=0)

label = tk.Label(rootUI, text="User Name", font=("Arial", 25))
label.pack()

save_button = tk.Button(rootUI, text="Save", command=player_name_save)
save_button.pack()

# tk.Entry is the input field GUI equivalent of input(var)

rootUI.mainloop()

