import tkinter as tk

# Function to handle the conversion
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km:.2f}")

# Create the main window
window = tk.Tk()
window.title("Miles to Kilometer Converter")

# Create an entry widget for miles input
miles_input = tk.Entry(width=7)
miles_input.grid(column=1, row=0)

# Create a label for "Miles"
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create a label for "is equal to"
is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Create a label to display the result in kilometers
kilometer_result_label = tk.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Create a label for "Km"
kilometer_label = tk.Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Create a button to trigger the conversion
calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Add padding around the window
window.config(padx=20, pady=20)

# Start the main loop
window.mainloop()
