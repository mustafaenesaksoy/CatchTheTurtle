import turtle
from random import randint
import time

screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.bgcolor("white")
screen.bgcolor("light blue")
count = 0

myTurtle = turtle.Turtle('turtle')
scoreText = turtle.Turtle()
scoreText.hideturtle()
scoreText.up()

# .write("Score: ", font=("Ariel",15,"bold"))
timerText = turtle.Turtle()
timerText.hideturtle()
timerText.up()
locationNumber = 150
locationList = []
i = 1
while True:
    if count == 120:
        break
    if i == 1:
        locationList.append((locationNumber - count, locationNumber - count))
        i += 1
        count += 10
    elif i == 2:
        locationList.append((-locationNumber + count, -locationNumber + count))
        i += 1
        count += 10
    elif i == 3:
        locationList.append((locationNumber - count, -locationNumber + count))
        i += 1
        count += 10
    elif i == 4:
        locationList.append((-locationNumber + count, locationNumber - count))
        i = 1
        count += 10

score = 0


def scoreCount(x, y):
    global score
    score += 1

def updateScoreText():
    scoreText.clear()
    scoreText.write(f"Score : {score}", font=("Ariel", 15, "bold"))

myTurtle.up()
myTurtle.speed(0)
timer = 15

timerText.setpos(-20, 250)
scoreText.setpos(-20, 200)
while True:
    myTurtle.hideturtle()
    rand = randint(0, len(locationList) - 1)
    myTurtle.goto(locationList[rand])
    myTurtle.showturtle()
    time.sleep(1)
    timer -= 1
    timerText.clear()
    myTurtle.onclick(scoreCount)
    updateScoreText()
    timerText.write(f"Left time: {timer}", font=("Ariel", 15, "bold"))
    if timer == 0:
        myTurtle.hideturtle()
        break





screen.mainloop()
