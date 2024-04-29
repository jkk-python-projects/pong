from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from fontTools.ttLib import TTFont

font = TTFont('bit5x3.ttf')
font.save("test_font")



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# scoreboard.write("test_font", align='center', font=('Bit5x3', 72, "normal"))


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_left_score()


    # detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_right_score()







screen.exitonclick()
