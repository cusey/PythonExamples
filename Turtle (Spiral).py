import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()

print('*** Draw Spiral ***')

def drawSpiral(myTurtle, color, lineLen):
    print( 'lineLen = {}'.format(lineLen) )
    if lineLen > 0:
        myTurtle.color(color)
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, "red",lineLen- 50)
        
print('-'*20)

drawSpiral(alex , "green", 100)         # complete the second side of a rectangle

