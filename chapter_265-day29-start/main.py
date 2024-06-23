# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk

# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
  
# Create a canvas with specified dimensions
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

# Start the main loop
window.mainloop()
