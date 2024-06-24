import tkinter as tk
import requests
from PIL import Image, ImageTk

# Function to fetch a Kanye quote from the API
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Load and display the background image
background_img = Image.open("background.png")
background_img = ImageTk.PhotoImage(background_img)
canvas = tk.Canvas(width=300, height=414, highlightthickness=0)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Load and display the Kanye button image
kanye_img = Image.open("kanye.png")
kanye_img = ImageTk.PhotoImage(kanye_img)
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Run the main loop
window.mainloop()
