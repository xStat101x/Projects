import turtle
s = turtle.getscreen()
t = turtle.Turtle()

x = 0
y = 0
z = 0
t.speed(0)
t.pensize(5)

#begining adjustments
t.penup()
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(500)
t.lt(180)
t.pencolor('blue')

#horazontal lines
t.pendown()
while x < 9:
    t.fd(1000)
    t.penup()
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.pendown()
    t.fd(1000)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    x = x + 1

#positioning
t.penup()
t.lt(90)
t.fd(50)
t.rt(90)
t.lt(135)
t.fd(750)
t.rt(90)
t.pencolor('red')

#diagnal positive lines
while y < 15:
    t.fd(1500)
    t.penup()
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.pendown()
    t.fd(1500)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    y = y + 1

#more adjustments
t.penup()
t.setposition(0, -1000)
t.pencolor('green')
t.pendown()
t.setheading(135)

#diagnols negative lines
while z < 15:
    t.fd(1500)
    t.penup()
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.pendown()
    t.fd(1500)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    z = z + 1





input("Type quit to close.\n")