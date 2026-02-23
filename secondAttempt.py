import tkinter as tk
from tkinter import messagebox
import json, os

SAVE_FILE = "player_statz.json"

class PlayerStatzApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playerz Statz")
        self.root.resizable(False, False)
        self.status_var = tk.StringVar()
        self._build_ui()

    def _build_ui(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=8)
        for label, cmd in [("Clear", self.clear), ("Load", self.load),
                           ("Save", self.save), ("Delete", self.delete)]:
            tk.Button(btn_frame, text=label, width=7, command=cmd).pack(side=tk.LEFT, padx=3)

        fields = [("Player name", "name"), ("XP", "xp"), ("Score", "score")]
        self.entries = {}
        for label, key in fields:
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root, justify="center", width=24)
            entry.pack(pady=2)
            self.entries[key] = entry

        tk.Label(self.root, textvariable=self.status_var, fg="green").pack(pady=6)

    # ── helpers ──────────────────────────────────────────────────────────────

    def _get_data(self):
        return {key: entry.get() for key, entry in self.entries.items()}

    def _set_data(self, data):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, data.get(key, ""))

    def _set_status(self, msg):
        self.status_var.set(msg)
        self.root.after(3000, lambda: self.status_var.set(""))

    # ── actions ──────────────────────────────────────────────────────────────

    def save(self):
        data = self._get_data()
        if not data["name"]:
            messagebox.showwarning("Save", "Player name is required.")
            return
        records = self._load_file()
        records[data["name"]] = data
        with open(SAVE_FILE, "w") as file:
            json.dump(records, file, indent=2)
        self._set_status("Saved!")

    def load(self):
        name = self.entries["name"].get()
        if not name:
            messagebox.showwarning("Load", "Enter a player name to load.")
            return
        records = self._load_file()
        if name in records:
            self._set_data(records[name])
            self._set_status("Loaded!")
        else:
            messagebox.showinfo("Load", f'No record found for "{name}".')

    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.status_var.set("")

    def delete(self):
        name = self.entries["name"].get()
        if not name:
            messagebox.showwarning("Delete", "Enter a player name to delete.")
            return
        records = self._load_file()
        if name in records:
            if messagebox.askyesno("Delete", f'Delete record for "{name}"?'):
                del records[name]
                with open(SAVE_FILE, "w") as file:
                    json.dump(records, file, indent=2)
                self.clear()
                self._set_status("Deleted!")
        else:
            messagebox.showinfo("Delete", f'No record found for "{name}".')

    def _load_file(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE) as file:
                return json.load(file)
        return {}


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("260x280")
    PlayerStatzApp(root)
    root.mainloop()