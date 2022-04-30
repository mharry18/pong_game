from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def hit_paddle(self):
        if self.x_move > 0:
            self.x_move += 5
        else:
            self.x_move -= 5
        if self.y_move > 0:
            self.y_move += 5
        else:
            self.y_move -= 5

    def reset_ball(self):
        if self.x_move < 0:
            self.x_move = 10
        else:
            self.x_move = -10
        self.y_move = 10
        self.goto(0, 0)
