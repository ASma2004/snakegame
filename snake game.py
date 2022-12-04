#importing libraries
#from ast import if
import turtle
import random
import time
#creating turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width= 700, height = 700)
screen.tracer(0)
turtle.bgcolor('green')
##creating a border for our game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()
#score
Score = 0
Delay = 0.1
#snake
snake=turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
#food
Fruit=turtle.Turtle()
Fruit.speed(0)
Fruit.shape('circle')
Fruit.color('red')
Fruit.penup()
Fruit.goto(30,30)

old_fruit = []
#scoring
Scoring = turtle.Turtle()
Scoring.speed(0)
Scoring.color("black")
Scoring.penup()
Scoring.hideturtle()
Scoring.goto(0,300)
Scoring.write("Score:",align="center",font=("Courier",24,"bold"))

######define how to move

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        Y = snake.ycor()
        snake.sety(Y + 20)

    if snake.direction == "down":
        Y = snake.xcor()
        snake.setx(Y - 20)

    if snake.direction == "right":
        X = snake.xcor()
        snake.setx(X + 20)

    if snake.direction == "right":
        X = snake.xcor()
        snake.setx(X - 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

#main loop

while True:
    screen.update()
            #snake and fruit coliisions
if snake.distance(fruit)< 20:
                X = random.randint(-290,270)
                Y = random.randint(-240,240)
                Fruit.goto(x,y)
                Scoring.clear()
                Score+=1
                Scoring.write("Score:{}".format(score), align=="center",font=("Courier",24,"bold"))
                Delay-=0.001
                
                ## creating new_ball
                New_fruit = turtle.Turtle()
                New_fruit.speed(0)
                New_fruit.shape('square')
                New_fruit.color('red')
                New_fruit.penup()
                old_fruit.append(new_fruit)
                

        #adding ball to snake
        
for index in range(len(old_fruit)-1,0,-1):
                A = old_fruit[index-1].xcor()
                B = old_fruit[index-1].ycor()

                old_fruit[index].goto(a,b)
                                     
if len(old_fruit)>0:
                A= snake.xcor()
                B = snake.ycor()
                old_fruit[0].goto(a,b)
snake_move()

        ##snake and border collision    
if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                Scoring.goto(0,0)
                Scoring.write(" GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## snake collision
for food in old_fruit:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('turquoise')
                        Scoring.goto(0,0)
                        Scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


                
time.sleep(delay)

turtle.Terminator()
