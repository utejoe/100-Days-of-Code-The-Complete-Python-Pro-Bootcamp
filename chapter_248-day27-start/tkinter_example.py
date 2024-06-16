import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My first GUI program")
root.minsize(500, 300)

# Create a label widget
my_label = tk.Label(root, text="I am a label", font=("Arial", 24, "bold"))

# Display the label using pack geometry manager
my_label.pack()

# Start the Tkinter event loop
root.mainloop()
