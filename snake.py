import turtle
import time
import random
import chime

body = []

# zapínací zvuk
chime.success()
chime.theme("mario")

# Definice hrací plochy, hada, dvou jídel, mystery boxu a skóre
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

# Pohyb hada
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

# Smrt
def chcipni():
    chime.error()
    chime.theme("mario")
    pen.clear()
    pen.write(f"        Score: {score}\n    GAME OVER",  align="center", font=("calibri", 24, "bold"))
    turtle.exitonclick()

# Pohyb hada
def move(i):
    previousPosition = snake.position()

    for member in body:
        currentPosition = member.position()
        member.setposition(previousPosition)
        previousPosition = currentPosition

    snake.forward(i)
# Přidání bodu
def addPoint(a):
    global score, pen, member, body
    score += a
    if score < 0:
        score = 0
    pen.clear()
    pen.write(f"Skore: {score}", align="center", font=("calibri", 24, "bold")) 
    for i in range(a):    
        member = turtle.Turtle()
        member.penup()
        member.shape("square")
        member.color("black")
        member.setposition(snake.position())
        body.insert(0, member)
    chime.success()
    chime.theme("mario")

# Hlavní smyčka
while True:
    window.update()

# Narážení do stěn
    if snake.ycor() > 415 or snake.ycor() < -405 or snake.xcor() > 692 or snake.xcor() < -692:        
        chcipni()

# Jezení jídla a mystery boxu
    elif snake.distance(food) < 20:
        
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        food.goto(x,y)
        addPoint(1)
        
    elif snake.distance(food2) < 20:
        
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        food2.goto(x,y)
        addPoint(1)
    
    elif snake.distance(mystery) < 20:
        x = random.randint(-712,712)
        y = random.randint(-405,405)
        mystery.goto(x,y)
        kolik = random.randint(0, 5)
        addPoint(kolik)
        
#kousání do těla
    for member in body[5:]:
        if snake.distance(member.position()) < 1:
            chcipni()

# Zrychlování       
    if score < 10:
        move(2)
    
    elif score > 30:
        move(6)

    else:
        move(score/5)
    
    time.sleep(0.01)
