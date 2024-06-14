import turtle
import random

# Initialize the turtle
tim = turtle.Turtle()
tim.speed("fastest")  # Fastest drawing speed
tim.pensize(15)       # Set the pen size to 15

# List of colors to choose from
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "black"]

# Directions (0, 90, 180, 270 degrees)
directions = [0, 90, 180, 270]

# Function to perform a random walk
def random_walk(steps, step_length):
    for _ in range(steps):
        tim.color(random.choice(colors))  # Choose a random color
        tim.forward(step_length)          # Move forward by step_length
        tim.setheading(random.choice(directions))  # Set a random heading (direction)

# Perform a random walk with 200 steps, each of 30 units
random_walk(200, 30)

# Keep the window open until clicked
turtle.mainloop()
