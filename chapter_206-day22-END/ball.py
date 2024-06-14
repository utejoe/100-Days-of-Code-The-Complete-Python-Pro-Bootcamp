import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.1  # Initial speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()

    def detect_collision_paddle(self, r_paddle, l_paddle):
        if (self.distance(r_paddle) < 50 and self.xcor() > 320) or (self.distance(l_paddle) < 50 and self.xcor() < -320):
            self.bounce_x()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Gradually increase speed

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset speed
        self.x_move = 2
        self.y_move = 2
