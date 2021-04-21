# Imports the needed functions
import turtle
from random import *


# Named constants
sWidth = 600
sHeight = 600
tWidth = 35
forceFactor = 30
turSpeed = 1
score = 0

# Setup the window
turtle.setup(sWidth,sHeight)

def runGame():
    global score

    # Randomly chooses a position for the target
    target_bLeft_X = randint(-200,200)
    target_bLeft_Y = randint(-200,200)
    
    # Clears the screen, then draw the target
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(target_bLeft_X,target_bLeft_Y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(tWidth)
    turtle.setheading(90)
    turtle.forward(tWidth)
    turtle.setheading(180)
    turtle.forward(tWidth)
    turtle.setheading(270)
    turtle.forward(tWidth)
    turtle.penup()

    # Center the turtle
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.showturtle()
    turtle.speed(turSpeed)

    # Gets the user's input and calculates distance
    turAngle = float(input("Enter the projectile's angle (-360 to 360): "))
    turForce = float(input("Enter the projectile's force (1-10): "))
    distance = turForce * forceFactor

    # Sets and launches the turtle
    turtle.setheading(turAngle)
    turtle.pendown()
    turtle.forward(distance)

    # Determines if the target was hit or not
    print()
    if (turtle.xcor() >= target_bLeft_X and
        turtle.xcor() <= (target_bLeft_X + tWidth) and
        turtle.ycor() >= target_bLeft_Y and
        turtle.ycor() <= (target_bLeft_Y + tWidth)):
            print("Target hit! :D")
            score += 100
            print("You earned 100 points! Your current score is: ",score)
    else:
            print("Target missed D\':")
            print("Your current score is: ",score)

    playAgain = input("Would you like to try again? (Yes or No) ")
    if playAgain == "Yes":
        print()
        runGame()
    else:
        print("Thanks for playing! Your final score was ",score)

runGame()
