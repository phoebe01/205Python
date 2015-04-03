from graphics import *
import random


# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
myarray = datafile.readlines()
for line in datafile:
    print(line)


while True:
    
    
    randNum = random.randint(0,25)
    float(myarray[randNum])
    
    box = Rectangle(Point(0,20),Point(float(myarray[0]),30))
    box.setOutline(color_rgb(255,0,0))
    box.draw(window)
    box = Rectangle(Point(0,20),Point(float(myarray[1]),30))
    box.setOutline(color_rgb(255,0,0))
    box.draw(window)    
    box = Rectangle(Point(0,20),Point(float(myarray[2]),30))
    box.setOutline(color_rgb(255,0,0))
    box.draw(window)
    
    
    
    # line = Line(Point(200,200),Point(250,280))
    #line.setWidth(float(myarray[randNum]))
    #line.draw(window)
    
    
    
    
    
    
    #text = Text(Point(50,200),"Hello")
   # text.draw(window)

    
#    ball = Circle(Point(float(myarray[randNum]),100), 30)
 #   ball.setFill(color_rgb(255,255,0))
  #  ball.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()