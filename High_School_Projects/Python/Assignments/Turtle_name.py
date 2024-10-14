import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.penup()
t.left(180)
t.forward(400)
t.right(90)

#letter R
def draw_r():
    t.pendown()
    t.forward(200)
    t.right(90)
    t.circle(-55, 180)
    t.left(90)
    t.left(35)
    t.forward(115)
draw_r()

#move the turtle
t.penup()
t.left(30)
t.left(90)
t.forward(100)
t.right(65)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)

#letter E
def draw_e():
    t.pendown()
    t.forward(100)
    t.left(90)
    t.circle(50, 330)
    t.right(60)
draw_e()

#move the turtle
t.penup()
t.forward(100)
t.left(90)
t.forward(50)
t.right(135)

#letter X
def draw_x():
    t.pendown()
    t.forward(100)
    t.left(135)
    t.penup()
    t.forward(75)
    t.left(135)
    t.pendown()
    t.forward(100)
draw_x()

#move the turtle
t.penup()
t.left(135)
t.forward(250)
t.left(90)

#letter K
def draw_k():
    t.pendown()
    t.forward(200)
    t.right(180)
    t.forward(100)
    t.left(45)
    t.forward(130)
    t.left(180)
    t.forward(130)
    t.right(90)
    t.forward(130)
draw_k()

#Move the turtle
t.penup()
t.right(45)
t.right(90)
t.forward(185)
t.left(90)
t.forward(10)
t.dot()
t.forward(50)

























input("Type quit to close.\n")