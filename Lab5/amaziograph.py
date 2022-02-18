# Done by anguslaw63631
import turtle

turtle.setup(800,600)    # Set the width and height be 800 x 600

number_of_divisions = 8  # The number of subdivisions around the centre
turtle_width = 3         # The width of the turtles

# Don't show the animation
turtle.tracer(False)

# Draw the background lines

backgroundLineTurtle = turtle.Turtle()

backgroundLineTurtle.width(1)

backgroundLineTurtle.down()
backgroundLineTurtle.color("gray84") # Draw the centered line
for i in range(number_of_divisions):
    backgroundLineTurtle.forward(500)
    backgroundLineTurtle.backward(500)
    backgroundLineTurtle.left(360 / number_of_divisions)

backgroundLineTurtle.up()

# Show the instructions
backgroundLineTurtle.color("purple")
backgroundLineTurtle.goto(-turtle.window_width()/2+50, 100)
backgroundLineTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to middle
c - clear all drawings made by the 8 drawing turtles
""", font=("Arial", 14, "normal"))

backgroundLineTurtle.hideturtle()

# Set up a turtle for handling message on the turtle screen
textTurtle = turtle.Turtle()
# This sets the colour of the text to red
textTurtle.color("red")
# We do not want it to show/draw anything, except the message text
textTurtle.up() 
# Set it the be at center, near the colour selections
textTurtle.goto(0, -200)
# We do not want to show it on the screen
textTurtle.hideturtle()

# Part 2 Preparing the drawing turtles

# The drawing turtles are put in a list
allDrawingTurtles = [] 

# Part 2.1 Add the 8 turtles in the list
# Please finish this part
for _ in range(number_of_divisions):
    newTurtle = turtle.Turtle()

    newTurtle.speed(0)
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()

    allDrawingTurtles.append(newTurtle)

    
# Part 2.2 Set up the first turtle for drawing
# Please finish this part
dragTurtle = allDrawingTurtles[0]
dragTurtle.showturtle()
dragTurtle.shape("circle")
dragTurtle.shapesize(2,2)

# Part 3 Preparing the basic drawing system
# Set up the ondrag event
# Please finish this part

def draw(x,y):
    dragTurtle.ondrag(None)
    turtle.tracer(False)
    dragTurtle.goto(x,y)
    textTurtle.clear()
    x_transform = [1, 1, -1, -1, 1, 1, -1, -1] # This represents + + - - + + - -
    y_transform = [1, -1, 1, -1, 1, -1, 1, -1] # This represents + - + - + - + -

    for i in range(1,number_of_divisions):
        if i < 4:
            new_x = x * x_transform[i] # x with sign change
            new_y = y * y_transform[i] # y with sign change
    	
        else:
            new_x = y * y_transform[i] # Note that we assign y as new x
            new_y = x * x_transform[i] # Note that we assign x as new y
        allDrawingTurtles[i].goto(new_x, new_y)
    turtle.tracer(True)    
    dragTurtle.ondrag(draw)
dragTurtle.ondrag(draw)

# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    # Please finish this part
    for thisturtle in allDrawingTurtles:
        thisturtle.clear()
    textTurtle.clear() # clear the previous message
    textTurtle.write("The screen is cleared", \
                       align="center", font=("Arial", 14, "normal"))
    
turtle.onkeypress(clearDrawing, 'c')

# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    # Please finish this part
    for thisturtle in allDrawingTurtles:
        thisturtle.up()
        thisturtle.goto(0,0)
        thisturtle.down()
    textTurtle.clear() # clear the previous message
    textTurtle.write("All 8 drawing turtles returned to middle", \
                       align="center", font=("Arial", 14, "normal"))    

turtle.onkeypress(goToMiddle, 'm')

# Part 4 handling the colour selection
# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "orange red", "lawn green", "medium purple", "light sky blue", "orchid", "gold"]

# Part 4.2 Set up the onclick event
# Please finish this part
def handleColourChange(x,y):
    for i in range(len(colours)):
        if x <= (-130 + 50 * i):
            for thisturtle in allDrawingTurtles:
                thisturtle.color(colours[i])
            break


# Part 5.4 change a colour in the colour selection
def changeColour():
    # Please finish this part
    colorIndex = turtle.textinput("Change color", "Please type the index number of the turtle: (0-6)")
    while  int(colorIndex) > 6 or int(colorIndex) < 0:
        colorIndex = turtle.textinput("Change color", "Wrong Index! Please type the index number of the turtle: (0-6)")
    if colorIndex != None:    
        colorCode = turtle.textinput("Change color", "Please type the color you want to use e.g. LightBlue2:")
        if colorCode != None:
            colours[int(colorIndex)] = colorCode
            textTurtle.write("The colour for that button has been changed, click on the button to use it", \
                               align="center", font=("Arial", 14, "normal"))
            colourSelectionTurtles[int(colorIndex)].color(colours[int(colorIndex)])



    turtle.listen()

turtle.onkeypress(changeColour, 's')

# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []
# Please finish this part
for i in range(len(colours)):
    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(2,2)
    t.up()
    t.color(colours[i])
    
    t.goto(-150 + 50*i,-250)
    
    t.onclick(handleColourChange)
    colourSelectionTurtles.append(t)

turtle.tracer(True)
turtle.listen()

turtle.done()

