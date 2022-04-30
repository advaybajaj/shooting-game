#Turtle Graphics game

#import libraries
import turtle
import random

print("Catch the virus to defeat it!")
print("Press the left and right arrow keys to change direction.")
print("Press the Up and Down arrow keys to speed-up or slow-down.")
print("Check out your score at the top-left corner of the screen and try to beat your own-best score!")

#Set up screen
background = turtle.Screen()
background.bgcolor("black")
background.bgpic("bgpic.gif")
background.tracer(3)

#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(2)
mypen.color("white")
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("orange")
player.shape("triangle")
player.penup()
player.speed(0)
player.shapesize(0.85, 0.85, 1.5)
speed = 1

score = 0

#create goals
max_goals = 10
goals = []

for count in range(max_goals):
    goals.append(turtle.Turtle())
    goals[count].color('lightblue')
    goals[count].shape('circle')
    goals[count].shapesize(0.65, 0.65, None)  
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))


#define functions
def TurnLeft():
    player.left(22.5)

def TurnRight():
    player.right(22.5)

def IncreaseSpeed():
    global speed
    speed += 1

def DecreaseSpeed():
    global speed
    speed -= 1

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

#set keyboard bindings
turtle.listen()
turtle.onkey(TurnLeft, "Left")
turtle.onkey(TurnRight, "Right")
turtle.onkey(IncreaseSpeed, "Up")
turtle.onkey(DecreaseSpeed, "Down")


while True:
    #move player
    player.forward(speed)
    
    #boundary check(for player)
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)

    #move the goal around
    for count in range(max_goals):
        goals[count].forward(1.5)

        #boundary check(for goal)
        if goals[count].xcor() > 290 or goals[count].xcor() <-290:
            goals[count].right(180)
        if goals[count].ycor() > 290 or goals[count].ycor() <-290:
            goals[count].right(180)

        if is_collided_with(player, goals[count]):
            goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            goals[count].right(random.randint(0, 360))
            score += 1
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

delay = input("Press enter to finish!")