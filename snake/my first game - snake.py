import turtle
import random
import time

# Screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("Snake trial")
wn.bgcolor("skyblue")
wn.tracer()

# Snake's head
head = turtle.Turtle()
head.speed(0)
head.penup()
head.shape("square")
head.color("black")
head.goto(0, 0)
head.direction = "stop"

# tail
segments = []

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0, 250)
pen.write("Score: 0 High Score: 0", align = "center", font=("courier", 24, "bold"))

# default scores
score =0
high_score = 0

# delay
delay = 0.1

# functions
def snake_up():
    if head.direction != "down":
        head.direction = "up"


def snake_down():
    if head.direction != "up":
        head.direction = "down"


def snake_right():
    if head.direction != "left":
        head.direction = "right"


def snake_left():
    if head.direction != "right":
        head.direction = "left"


# snake movement
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


# key bindings
wn.listen()
wn.onkeypress(snake_up, "Up")
wn.onkeypress(snake_down, "Down")
wn.onkeypress(snake_right, "Right")
wn.onkeypress(snake_left, "Left")


# Main game loop
while True:
    wn.update()

    # boundaries
    if not -280.5 < head.xcor() < 285 or not -245 < head.ycor() < 245:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # # clear the segments
        segments.clear()

        # reset score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "bold"))

    # eat food
    if head.distance(food) < 15:
        # respawn food at random spot
        y = random.randint(-240, 240)
        x = random.randint(-290, 290)
        food.goto(x, y)

        # score increment
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "bold"))

        # add a segment
        segment = turtle.Turtle()
        segment.penup()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segments.append(segment)

        delay -= 0.001

        wn.update()


    # eat itself
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # reset score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "bold"))

            delay = 0.1

    # set the segment 0 at the position of the head
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)
    wn.update()
