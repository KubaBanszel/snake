import turtle
import time
import random
import chime

body = []

chime.success()
chime.theme("mario")

scr = turtle.Screen()
window = turtle.Screen()
window.title("Hadik vrum vrum")
window.bgcolor("pink")
window.setup(width=1425, height=850)
window.listen()
window.tracer(0)

snake = turtle.Turtle()
snake.penup()
snake.shape("square")
snake.color("black")
snake.goto(0,0)


food = turtle.Turtle()
food.penup()
food.shape("circle")
food.color("red")
food.goto(200,200)

food2 = turtle.Turtle()
food2.penup()
food2.shape("circle")
food2.color("red")
food2.goto(-200,-200)

mystery = turtle.Turtle()
mystery.penup()
mystery.shape("circle")
mystery.color("yellow")
mystery.goto(200,-200)

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))


def up():
    if snake.heading() != 270:
        snake.setheading(90)

window.onkeypress(up, "Up")

def left():
    if snake.heading() != 0:
        snake.setheading(180)

window.onkeypress(left, "Left")

def right():
    if snake.heading() != 180:
        snake.setheading(0)

window.onkeypress(right, "Right")

def down():
    if snake.heading() != 90:
        snake.setheading(270)

window.onkeypress(down, "Down")

def chcipni():
    pen.clear()
    pen.write(f"        Score: {score}\n    GAME OVER",  align="center", font=("calibri", 24, "bold"))
    turtle.exitonclick()

def move(i):
    previousPosition = snake.position()

    for member in body:
        currentPosition = member.position()
        member.setposition(previousPosition)
        previousPosition = currentPosition

    snake.forward(i)

def addPoint(a):
    global score
    global pen
    global member
    global body
    score += a
    if score < 0:
        score = 0
    pen.clear()
    pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold")) 
    member = turtle.Turtle()
    member.penup()
    member.shape("square")
    member.color("orange")
    member.setposition(snake.position())
    body.insert(0, member)
    chime.success()
    chime.theme("mario")

while True:
    window.update()

# Narážení do stěn
    if snake.ycor() > 415 or snake.ycor() < -405 or snake.xcor() > 692 or snake.xcor() < -692:        
        chcipni()

# Jezení jídla
    elif snake.distance(food) < 20:
        addPoint(1)
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        food.goto(x,y)
        
        
    elif snake.distance(food2) < 20:
        addPoint(1)
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        food2.goto(x,y)
        
    
    elif snake.distance(mystery) < 20:
        kolik = random.randint(-5, 5)
        addPoint(kolik)
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        mystery.goto(x,y)
        
        
#kousání do těla
    for member in body[5:]:
        if snake.distance(member.position()) < 15:
            chcipni()

# Zrychlování       
    if score == 0:
        move(1)
    
    elif score == 1:
        move(2)

    elif score >= 10:
        move(10)

    else:
        move(score)
    
    time.sleep(0.01)
