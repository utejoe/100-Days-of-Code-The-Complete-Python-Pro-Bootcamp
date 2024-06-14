import turtle
import random

# Initialize the turtle
tim = turtle.Turtle()
tim.speed(5)  # Fastest drawing speed

# List of colors to choose from
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "black"]

# Function to draw a shape with a given number of sides
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# Main loop to draw shapes from triangle (3 sides) to decagon (10 sides)
for sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(sides)

# Keep the window open until clicked
turtle.mainloop()
