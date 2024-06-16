import tkinter as tk

# Initialize the window
window = tk.Tk()

# Create a label
my_label = tk.Label(text="I am a label")
my_label.pack()

# Function to be called when the button is clicked
def button_clicked():
    my_label.config(text="Button got clicked")

# Create a button
button = tk.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
