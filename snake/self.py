import turtle
import time

# create screen
wn = turtle.Screen()
wn.setup(width= 600, height=400)
wn.bgcolor("skyblue")
wn.title("Aiwei")
wn.tracer()


# pen for scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("White")
pen.goto(0, 150)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))

# score variables
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-280, 0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.goto(280, 0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


# ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.shape("circle")
ball.color("White")
ball.dx = 2
ball.dy = 2


# functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)

# key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boundaries
    if ball.ycor() > 192 or ball.ycor() < -192:
        ball.dy *= -1

    # bounce off the paddles
    if -260 > ball.xcor() and ball.dx < 0 and (paddle_a.ycor() - 50) < ball.ycor() < (paddle_a.ycor() + 50):
        ball.dx *= -1
    if 260 < ball.xcor() and ball.dx > 0 and (paddle_b.ycor() - 50) < ball.ycor() < (paddle_b.ycor() + 50):
        ball.dx *= -1

    # scoring
    if ball.xcor() > 290:
        ball.goto(0, 0)
        score_a += 1
        if score_a == 2:
            pen.clear()
            pen.write("Player A wins!", align="center", font=("courier", 24, "bold"))
            time.sleep(1.5)
            score_a, score_b = 0, 0
            ball.dx *= 2
            ball.dy *= 2
            pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))

        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.goto(0, 0)
        score_b += 1
        if score_b == 2:
            pen.clear()
            pen.write("Player B wins!", align="center", font=("courier", 24, "bold"))
            time.sleep(1.5)
            score_a, score_b = 0, 0
            ball.dx *= 2
            ball.dy *= 2
            pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))

        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
        ball.dx *= -1
