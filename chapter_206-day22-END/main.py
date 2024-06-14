import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Listen for keypress events
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    ball.detect_collision_wall()

    # Detect collision with paddles
    ball.detect_collision_paddle(r_paddle, l_paddle)

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()

screen.mainloop()
