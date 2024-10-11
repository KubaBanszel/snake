import turtle
import time
import random

window = turtle.Screen()
window.title("Mackas mi hada debile")
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
    snake.setheading(90)

window.onkeypress(up, "Up")

def left():
    snake.setheading(180)

window.onkeypress(left, "Left")

def right():
    snake.setheading(0)

window.onkeypress(right, "Right")

def down():
    snake.setheading(270)

window.onkeypress(down, "Down")

def move():
    speed = 4
    snake.forward(speed)

while True:
    window.update()

    if snake.ycor() > 425 or snake.ycor() < -425 or snake.xcor() > 712 or snake.xcor() < -712:
        time.sleep(0.5)
        snake.goto(0,0)
        if score > 2:
            score -= 2
            pen.clear()
            pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))  
        elif score == 1:
            score = 0
            pen.clear()
            pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))
        else:
            score =0
            pen.clear()
            pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))

    if snake.distance(food) < 20:
        x = random.randint(-712,712)
        y = random.randint(-425,425)
        food.goto(x,y)
        score += 1
        pen.clear()
        pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold"))   
        
            
    move()
    time.sleep(0.01)
