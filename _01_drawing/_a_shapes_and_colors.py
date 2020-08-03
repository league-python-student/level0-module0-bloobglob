import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    lucas = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    lucas.shape('turtle')
    # Set your turtle's speed using .speed(2)
    lucas.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    lucas.color('green')
    lucas.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    lucas.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    lucas.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        lucas.forward(100)
        lucas.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    lucas.goto(100, 100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    lucas.begin_fill()
    lucas.circle(50, 360, 30)
    lucas.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    lucas.circle(25, 360, 5)
    lucas.penup()
    lucas.goto(200, 0)
    lucas.pendown()
    lucas.circle(150, 180, 30)
    lucas.penup()
    lucas.goto(35, -15)
    lucas.pendown()
    lucas.circle(15, 360, 30)
    lucas.penup()
    lucas.pendown()
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
