import tkinter as tk

# Initialize the window
window = tk.Tk()

# Create an entry widget
entry = tk.Entry(width=10)
entry.pack()

# Function to be called when the button is clicked
def button_clicked():
    new_text = entry.get()  # Get text from entry
    my_label.config(text=new_text)

# Create a label
my_label = tk.Label(text="I am a label")
my_label.pack()

# Create a button
button = tk.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
