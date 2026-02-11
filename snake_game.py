import turtle
import time
import random
delay = 100  
score = 0
high_score = 0
wn = turtle.Screen()
wn.title("Snake Game - Optimized")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
head.last_move = "stop" 
def go_up():
    if head.last_move != "down":
        head.direction = "up"
def go_down():
    if head.last_move != "up":
        head.direction = "down"
def go_left():
    if head.last_move != "right":
        head.direction = "left"
def go_right():
    if head.last_move != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    head.last_move = head.direction
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
def game_loop():
    global score, high_score, delay

    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()
        return
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)
        if delay > 50: 
            delay -= 1
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()
            return
    wn.ontimer(game_loop, delay)
def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    head.last_move = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 100
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    wn.ontimer(game_loop, delay)
game_loop()
wn.mainloop()
