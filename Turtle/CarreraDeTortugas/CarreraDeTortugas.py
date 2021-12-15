import turtle
import random

# creo pantalla
screen = turtle.Screen()
screen.title("Carrera De Tortugas")
screen.bgcolor("grey")


# creo jugadores
turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.shape("turtle")
turtle1.color("green", "green")
turtle1.shapesize(2,2,2)
turtle1.pensize(3)

turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.shape("turtle")
turtle2.color("blue", "blue")
turtle2.shapesize(2,2,2)
turtle2.pensize(3)


# dibujo de metas
turtle1.penup()
turtle1.goto(200,200)
turtle1.pendown()
turtle1.circle(40)

turtle2.penup()
turtle2.goto(200,-200)
turtle2.pendown()
turtle2.circle(40)


# envio al incio de la carrera
turtle1.penup()
turtle1.goto(-200,225)
turtle1.showturtle()

turtle2.penup()
turtle2.goto(-200,-175)
turtle2.showturtle()


# dado
dado = [1,2,3,4,5,6]


# implementacion pos()
for i in range(20):
  if turtle1.pos()>=(200,200):
    print("Tortuga verde ganó")
    break
  elif turtle2.pos()>=(200,-200):
    print("Tortuga azul ganó")
    break
  else:
    turno1 = input("Press enter para avanzar")
    turno1 = random.choice(dado)
    print("Salió: ", turno1, "\nAvanzas: ",turno1*10) 
    turtle1.pendown()
    turtle1.forward(turno1*10) 
    
    turno2 = input("Press enter para avanzar")
    turno2 = random.choice(dado)
    print("Salió: ", turno2, "\nAvanzas: ",turno2*10) 
    turtle2.pendown()
    turtle2.forward(turno2*10) 



turtle.done()