import turtle
import random

# Initialize the turtle
tim = turtle.Turtle()
tim.speed("fastest")  # Fastest drawing speed
tim.pensize(15)       # Set the pen size to 15

# Set the color mode to 255 to use RGB values from 0 to 255
turtle.colormode(255)

# Function to generate a random color using RGB
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Directions (0, 90, 180, 270 degrees)
directions = [0, 90, 180, 270]

# Function to perform a random walk
def random_walk(steps, step_length):
    for _ in range(steps):
        tim.color(random_color())  # Choose a random color
        tim.forward(step_length)   # Move forward by step_length
        tim.setheading(random.choice(directions))  # Set a random heading (direction)

# Perform a random walk with 200 steps, each of 30 units
random_walk(200, 30)

# Keep the window open until clicked
turtle.mainloop()
