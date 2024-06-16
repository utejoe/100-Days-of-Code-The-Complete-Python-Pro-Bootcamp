import tkinter as tk

# Initialize the window
window = tk.Tk()

# Create a label with initial text
my_label = tk.Label(text="I am a label")
my_label.pack()

# Change text using dictionary-style access
my_label["text"] = "New text"

# Change text using the config method
my_label.config(text="Another new text")

window.mainloop()
