# COMP1021 Lab 2 Python Sketchbook
# Name: anguslaw63631
# Student ID: 
# Email: 

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

##### Initialize the colour
fillcolor = "black"
turtle.pencolor("black")
turtle.fillcolor(fillcolor)

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        angle = input("Please enter the angle of rotation:")
        angle = int(angle)
        turtle.left(angle)

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        #
        width = input("Please enter the width of the rectangle:")
        width = int(width)
        height = input("Please enter the height of the rectangle:")
        height = int(height)
        for i in range(1,3):
            turtle.begin_fill()
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
            turtle.end_fill()

        
        
        #

    ##### Handle the circle option
    if option == "c":
        print()

        #
        radius = input("Please enter the radius of the circle:")
        radius = int(radius)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        #

    ##### Handle the pen colour option
    if option == "p":
        print()

        #
        pencolor = input("Please enter a colour name for the pen colour:")
        turtle.pencolor(pencolor)
        #

    ##### Handle the fill colour option
    if option == "f":
        print()

        #
        fillcolor = input("Please enter a colour name for the fill colour:")
        turtle.fillcolor(fillcolor)
        #

    if option == "g":
        print()
        fpsize = input("Please enter the size of the flower petal:")
        fpsize = int(fpsize)
        for i in range(12):
            for j in range(3):
                turtle.forward(fpsize)
                turtle.left(120)
            turtle.left(30)

    if option == "e":
        print()
        esize = input("Please enter the size of the explosion (>150):")
        esize = int(esize)
        for colour in ["cyan","DeepSkyBlue","red"]:
            for i in range(1,5):
                turtle.color(colour + str(i))
                turtle.dot(esize)
                esize = esize - 10


    if option == "a":
        print()
        turtle.pencolor("white")
        turtle.right(180)
        turtle.forward(180)
        turtle.right(180)
        turtle.pencolor("black")
        turtle.right(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(100)
        turtle.pencolor("white")
        turtle.forward(20)
        turtle.pencolor("black")
        turtle.left(60)
        turtle.forward(150)
        turtle.right(120)
        turtle.forward(150)
        turtle.left(180)
        turtle.forward(60)
        turtle.left(60)
        turtle.forward(90)
        turtle.left(180)
        turtle.forward(90)
        turtle.pencolor("white")
        turtle.forward(30)
        turtle.pencolor("black")
        turtle.right(60)
        turtle.forward(100)
        turtle.left(110)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(60)
        turtle.left(110)
        turtle.forward(100)
        

              

turtle.done()
