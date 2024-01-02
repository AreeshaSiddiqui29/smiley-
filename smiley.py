# Import the turtle module
import turtle

# Create a turtle instance
t = turtle.Turtle()

# Set the filling color to yellow
t.fillcolor('yellow')

# Begin filling the shape with the specified color
t.begin_fill()

# Draw a circle with a radius of 100
t.circle(100)

# End the filling of the shape
t.end_fill()

# Lift the pen (stop drawing)
t.penup()

# Move the turtle to the specified coordinates without drawing
t.goto(-40, 120)

# Put the pen down (start drawing)
t.pendown()

# Begin filling a circle with a radius of 10
t.begin_fill()

# Draw a small circle at (-40, 120)
t.circle(10)

# End the filling of the small circle
t.end_fill()

# Lift the pen
t.penup()

# Move the turtle to another set of coordinates without drawing
t.goto(40, 120)

# Put the pen down
t.pendown()

# Begin filling a circle with a radius of 10
t.begin_fill()

# Draw a small circle at (40, 120)
t.circle(10)

# End the filling of the small circle
t.end_fill()

# Lift the pen
t.penup()

# Move the turtle to a new position without drawing
t.goto(-30, 85)

# Put the pen down and rotate the turtle 90 degrees to the right
t.pendown()
t.right(90)

# Draw part of a circle with a radius of 30 and an arc of 190 degrees
t.circle(30, 190)

# Finish drawing
turtle.done()

