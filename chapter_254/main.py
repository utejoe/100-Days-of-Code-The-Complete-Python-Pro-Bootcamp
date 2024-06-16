import tkinter as tk

# Function to handle button click
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

# Initialize the window
window = tk.Tk()
window.title("My Tkinter App")

# Create a label
my_label = tk.Label(text="I am a label")
my_label.grid(column=0, row=0, padx=10, pady=10)

# Create an entry
input = tk.Entry(width=10)
input.grid(column=1, row=1, padx=10, pady=10)

# Create a button
button = tk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=0, padx=10, pady=10)

# Adding a new button
new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0, padx=10, pady=10)

window.mainloop()
