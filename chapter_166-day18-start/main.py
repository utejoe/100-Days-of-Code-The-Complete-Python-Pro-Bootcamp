from turtle import Turtle, Screen

# Create a turtle object
timmy_the_turtle = Turtle()

# Create a screen object
screen = Screen()

# Set the shape of the turtle
timmy_the_turtle.shape("turtle")

# Set the color of the turtle
timmy_the_turtle.color("red")

# Move the turtle forward by 100 units
timmy_the_turtle.forward(100)

# Turn the turtle right by 90 degrees
timmy_the_turtle.right(90)

# Keep the window open until clicked
screen.exitonclick()
