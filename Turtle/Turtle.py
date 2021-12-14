import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")

screen.bgcolor("red")
screen.title("Turtle")

t.shapesize(3,3,3)
t.fillcolor("orange")
t.pencolor("white")
t.speed(2)

t.backward(100)
t.right(90)
t.forward(100)
t.fd(130)
t.goto(100,100)
t.circle(100)
t.left(50)
t.forward(100)
t.dot(30)
t.setx(-200)
t.begin_fill()
t.circle(50)
t.end_fill()

# t.hideturtle()
# t.showturtle()

turtle.done()