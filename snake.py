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

def move(i):
    speed = i
    snake.forward(speed)

while True:
    window.update()
# Narážení do stěn
    if snake.ycor() > 415 or snake.ycor() < -405 or snake.xcor() > 692 or snake.xcor() < -692:
        for i in range(30):
            snake.forward(i)
            snake.left(i) 
        
        snake.goto(0,0)
        pen.clear()
        pen.write(f"        Score: {score}\n    GAME OVER",  align="center", font=("calibri", 24, "bold"))
        turtle.exitonclick()
# Jezení jídla
    elif snake.distance(food) < 20:
        x = random.randint(-712,712)
        y = random.randint(-425,425)
        food.goto(x,y)
        score += 1
        pen.clear()
        pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))   
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
