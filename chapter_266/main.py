import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(8)]
    password_symbols = [random.choice(symbols) for _ in range(2)]
    password_numbers = [random.choice(numbers) for _ in range(2)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it okay to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Use the absolute path for the logo image
logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
logo_img = tk.PhotoImage(file=logo_path)

canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@example.com")
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
