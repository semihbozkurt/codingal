import turtle
arw=turtle.Turtle()

'''arw.speed(10)
arw.fillcolor("")
arw.begin_fill()

colors=["red","green","black","orange","blue"]

for i in range (50):
    arw.pencolor(colors[i%5])
    arw.forward(i*10+10)
    arw.left(144)

arw.end_fill()

turtle.done()
'''

arw.pensize(1)
arw.speed(0)
arw.fillcolor("purple")
arw.begin_fill()

colors=["red","green","black","orange","blue"]

for i in range (36):
    arw.pencolor(colors[i%5])
    arw.circle(100)
    arw.left(10)

arw.end_fill()

turtle.done()