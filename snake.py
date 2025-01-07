import turtle
import time
import random


scr = turtle.Screen()
window = turtle.Screen()
window.title("Mackas mi hadaa")
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

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,250)
pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))

body = []


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

while True:
    window.update()
# Narážení do stěn
    if snake.ycor() > 415 or snake.ycor() < -405 or snake.xcor() > 692 or snake.xcor() < -692:
        for i in range(30):
            snake.forward(i)
            snake.left(i) 
        
        snake.goto(0,0)
        chcipni()
# Jezení jídla
    elif snake.distance(food) < 20:
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        food.goto(x,y)
        score += 1
        pen.clear()
        pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold")) 
        member = turtle.Turtle()
        member.penup()
        member.shape("square")
        member.color("orange")
        member.setposition(snake.position())
        body.insert(0, member)
#kousání do těla
    for member in body[5:]:
        if snake.distance(member.position()) < 15:
            chcipni()
# Zrychlování       
    if score == 0:
        move(2)
    
    elif score == 1:
        move(3)

    elif score >= 10:
        move(10)

    else:
        move(score+1)
    time.sleep(0.01)
