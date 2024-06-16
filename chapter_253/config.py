import tkinter as tk

# Initialize the window
window = tk.Tk()

# Create a label
my_label = tk.Label(text="I am a label")
my_label.pack()

# Configure multiple properties at once
my_label.config(text="New text", font=("Arial", 24, "bold"), bg="yellow")

window.mainloop()
