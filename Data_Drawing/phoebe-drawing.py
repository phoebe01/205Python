from graphics import *
import random # imports modules needed




#Read and prints out the data from the data file
data = open("data.txt",'r')
array = data.readlines()
for line in data: 
    print(line)


# Creates the window
window = GraphWin("Visualisation", 600, 600)


#makes the shape appaear in random places, randow sizes and random colours.
for i in range(0,len(array)):
	blue = random.randint(0,255)
	green = random.randint(0,255)
	red = random.randint(0,255)
	randomNumberHeight = random.randint(50,550)
	randomNumberWidth = random.randint(0,550)
#draws the visualisation and displays it in the attached window
	ball = Circle(Point(randomNumberHeight,randomNumberWidth),float(array[i]))
	ball.setFill(color_rgb(blue,green,red))
	ball.draw(window)


# Waits until the mouse is clicked before closing the window
window.getMouse()
