import turtle
arw=turtle.Turtle()

arw.speed(0)
arw.fillcolor("orange")
arw.begin_fill


colors=["red","green","black","lightgreen","yellow","blue","purple","cyan"]
for i in range(50):
    arw.color(colors[i%8])
    arw.forward(i*3+6)
    arw.left(45)


arw.end_fill
turtle.done()
