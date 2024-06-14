import turtle

# Create a turtle object
tim = turtle.Turtle()

# Set the drawing speed
tim.speed(0)

# Define the length of each section
section_length = 10

# Repeat the drawing pattern multiple times
for _ in range(15):
    # Draw a section
    tim.forward(section_length)
    # Move without drawing
    tim.penup()
    tim.forward(section_length)
    # Resume drawing
    tim.pendown()

# Keep the window open until clicked
turtle.mainloop()
