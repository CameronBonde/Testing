import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

class PlayerStatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playerz Statz")
        self.root.geometry("300x250")

        # Variables to store player data
        self.player_name = tk.StringVar()
        self.xp = tk.IntVar(value=0)
        self.score = tk.IntVar(value=0)

        # File path for saving/loading
        self.file_path = None

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons
        tk.Button(button_frame, text="Clear", command=self.clear_fields).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Load", command=self.load_data).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Save", command=self.save_data).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Delete", command=self.delete_data).pack(side=tk.LEFT, padx=2)

        # Player name section
        tk.Label(self.root, text="Player name", fg="red").pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.root, textvariable=self.player_name)
        self.name_entry.pack(fill=tk.X, padx=10)

        # XP section
        tk.Label(self.root, text="XP", fg="red").pack(pady=(10, 0))
        self.xp_entry = tk.Entry(self.root, textvariable=self.xp)
        self.xp_entry.pack(fill=tk.X, padx=10)

        # Score section
        tk.Label(self.root, text="Score", fg="red").pack(pady=(10, 0))
        self.score_entry = tk.Entry(self.root, textvariable=self.score)
        self.score_entry.pack(fill=tk.X, padx=10)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="orange")
        self.status_label.pack(pady=10)

    def clear_fields(self):
        """Clear all input fields"""
        self.player_name.set("")
        self.xp.set(0)
        self.score.set(0)
        self.file_path = None
        self.update_status("Fields cleared")

    def load_data(self):
        """Load player data from a JSON file"""
        file_path = filedialog.askopenfilename(
            title="Select Player Data File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if not file_path:
            return

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

            self.player_name.set(data.get('player_name', ''))
            self.xp.set(data.get('xp', 0))
            self.score.set(data.get('score', 0))
            self.file_path = file_path
            self.update_status("Loaded!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def save_data(self):
        """Save player data to a JSON file"""
        if not self.player_name.get():
            messagebox.showwarning("Warning", "Please enter a player name")
            return

        # If no file path exists, ask for one
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(
                title="Save Player Data As",
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )

            if not self.file_path:  # User cancelled
                return

        try:
            data = {
                'player_name': self.player_name.get(),
                'xp': self.xp.get(),
                'score': self.score.get()
            }

            with open(self.file_path, 'w') as f:
                json.dump(data, f)

            self.update_status("Saved!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")

    def delete_data(self):
        """Delete the current player data file"""
        if not self.file_path or not os.path.exists(self.file_path):
            messagebox.showwarning("Warning", "No file to delete")
            return

        try:
            os.remove(self.file_path)
            self.clear_fields()
            self.update_status("File deleted!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file: {str(e)}")

    def update_status(self, message):
        """Update the status label with a message"""
        self.status_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerStatsApp(root)
    root.mainloop()
