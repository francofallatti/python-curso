import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

for i in range(4):
  t.forward(100)
  t.right(90)

# t.circle(100)
# t.circle(90)
# t.circle(80)
# t.circle(70)
# t.circle(60)
# t.circle(50)
# t.circle(40)
# t.circle(30)
# t.circle(20)
# t.circle(10)

i=0
while i<=100:
  t.circle(i)
  i+=10

turtle.done()