from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 330 or ball.distance(l_paddle) <= 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.hit_paddle()

    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.l_point()
        elif ball.xcor() < -380:
            scoreboard.r_point()
        ball.reset_ball()

    if scoreboard.l_score == 10:
        winning_player = "Player 1"
        scoreboard.game_over(winning_player)
        game_is_on = False
    elif scoreboard.r_score == 10:
        winning_player = "Player 2"
        scoreboard.game_over(winning_player)
        game_is_on = False

screen.exitonclick()