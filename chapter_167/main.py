from turtle import Turtle, Screen

# Create a turtle object
Tim = Turtle()

# Draw a square
for _ in range(4):
    Tim.forward(100)
    Tim.left(90)

# Keep the window open until clicked
Screen().exitonclick()

