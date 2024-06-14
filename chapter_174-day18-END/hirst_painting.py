import turtle as t
import random
import colorgram
import os

# Ensure the script is running in the correct directory
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
# Combine the script directory with the image filename to create an absolute path
image_path = os.path.join(script_dir, 'image.jpg')

# Extract colors from the image
# Extract up to 30 colors from the image
colors = colorgram.extract(image_path, 30)
# Create a list of RGB tuples from the extracted colors
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Set up the turtle screen
# Set the color mode to 255 to use RGB values
t.colormode(255)
# Create a screen object
screen = t.Screen()
# Set the background color of the screen to white
screen.bgcolor("white")

# Set up the turtle
# Create a turtle object
tim = t.Turtle()
# Set the speed of the turtle to the fastest
tim.speed("fastest")
# Lift the pen to avoid drawing lines between the dots
tim.penup()

# Function to create the spot painting
def draw_dot_painting(dot_count, dot_size, spacing):
    # Position the turtle to start the painting
    tim.setheading(225)  # Point the turtle to the bottom-left direction
    tim.forward(300)     # Move the turtle to the starting position
    tim.setheading(0)    # Point the turtle to the right direction
    number_of_dots = dot_count  # Number of dots to draw

    for dot in range(1, number_of_dots + 1):
        # Draw a dot with a random color from the extracted colors
        tim.dot(dot_size, random.choice(rgb_colors))
        # Move the turtle forward by the spacing value
        tim.forward(spacing)

        if dot % 10 == 0:  # Move to the next row after every 10 dots
            tim.setheading(90)    # Point the turtle upwards
            tim.forward(spacing)  # Move the turtle up by the spacing value
            tim.setheading(180)   # Point the turtle to the left direction
            tim.forward(spacing * 10)  # Move the turtle left by 10 times the spacing value
            tim.setheading(0)     # Point the turtle to the right direction again

# Call the function to draw the dot painting with 100 dots, each of size 20, and spaced 50 apart
draw_dot_painting(100, 20, 50)

# Exit the program when the screen is clicked
screen.exitonclick()
