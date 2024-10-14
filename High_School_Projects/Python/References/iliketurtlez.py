import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.right(90) #rt
t.forward(100) #fd
t.left(90) #lt
t.backward(100) #bw

t.circle(100) #draws a circle counterclockwise ssstarting at the bottom
t.dot(50) #puts a dot with a 50 pixel diameter. The turtle is the center of the dot.


t.pensize(10) #PEN size
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(200)
t.rt(90)
t.clear()
t.pen(pencolor="purple", fillcolor='orange', pensize=10, speed=9)
x = 0 
while x != 4:
    t.fd(200)
    t.rt(90)
    x = x + 1
t.rt(180)
t.fd(100)
t.begin_fill()
t.circle(100)
t.end_fill()







