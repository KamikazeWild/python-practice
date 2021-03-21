import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("chocolate")
wn.setup(width=800, height=600)
wn.tracer(0)

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="Center", font=("courier", 24, "normal"))
pen.color("white")

# Scoring
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-380, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(380, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)


# key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # boundary
    if ball.ycor() > 288:
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
        ball.dy *= -1

    if ball.ycor() < -288:
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
        ball.dy *= -1

    # scoring move
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("courier", 24, "normal"))
        if score_a == 5:
            pen.clear()
            pen.write("Player A wins!!!", align="center", font=("courier", 24, "normal"))
            time.sleep(1.5)
            pen.clear()
            ball.dx += 0.2
            ball.dy += 0.2
            score_a = 0
            score_b = 0
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center",
                      font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("courier", 24, "normal"))
        if score_b == 5:
            pen.clear()
            pen.write("Player B wins!!!", align="center", font=("courier", 24, "normal"))
            time.sleep(1.5)
            pen.clear()
            ball.dx += 0.2
            ball.dy += 0.2
            score_a = 0
            score_b = 0
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center",
                      font=("courier", 24, "normal"))

    # bounce off pedals
    if (360 < ball.xcor() < 370) and (
            paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(360)
        ball.dx *= -1
        winsound.PlaySound("paddle a.wav", winsound.SND_ASYNC)

    if (-360 > ball.xcor() > -370) and (
            paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-360)
        ball.dx *= -1
        winsound.PlaySound("paddle a.wav", winsound.SND_ASYNC)

    time.sleep(0.01)