import tkinter as tk

# Initialize the window
window = tk.Tk()

# Variable to store the state of the checkbox
check_state = tk.IntVar()

# Function to be called when the checkbox is toggled
def checkbox_toggled():
    print(check_state.get())  # Print the state of the checkbox (0 or 1)

# Create a checkbox
checkbox = tk.Checkbutton(text="Check me", variable=check_state, command=checkbox_toggled)
checkbox.pack()

window.mainloop()
