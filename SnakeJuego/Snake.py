import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

# creacion de pantalla y jugador
screen = turtle.Screen()
screen.setup(650, 650)
screen.bgcolor("black")
screen.title("Snake Game")

snake = turtle.Turtle()
snake.speed(1)
snake.shape("square")
snake.penup()
snake.direction = "stop"
snake.color("green")
cuerpo=[]

texto = turtle.Turtle()
texto.speed(0)
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.color("white")
texto.write("marcado: {} Marcador más alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))




# movimiento de la serpiente
def up():
  snake.direction = 'up'
def down():
  snake.direction = 'down'
def right():
  snake.direction = 'right'
def left():
  snake.direction = 'left'

def moviento():
  if snake.direction == 'up':
    y = snake.ycor()
    snake.sety(y+10)
  if snake.direction == 'down':
    y = snake.ycor()
    snake.sety(y-10)
  if snake.direction == 'right':
    x = snake.xcor()
    snake.setx(x+10)
  if snake.direction == 'left':
    x = snake.xcor()
    snake.setx(x-10)

screen.listen()#pone a la escucha a la pantalla
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")


# crear comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.speed(0)

while True:
  screen.update()
  
  if snake.xcor() > 325 or snake.xcor() < -325 or snake.ycor() > 325 or snake.ycor() < -325:
    time.sleep(2)
    for i in cuerpo:
      i.clear()
      i.hideturtle()
    snake.home()
    snake.direction = 'stop'
    cuerpo.clear()
    
    marcador=0
    texto.clear()
    texto.write("marcado: {} Marcador más alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))
  
  
  if snake.distance(comida)<20:
    Xcomida = random.randint(-250,250)
    Ycomida = random.randint(-250,250)
    comida.goto(Xcomida,Ycomida)
    
    nuevo_cuerpo = turtle.Turtle()
    nuevo_cuerpo.shape("square")
    nuevo_cuerpo.color("green")
    nuevo_cuerpo.penup()
    nuevo_cuerpo.goto(0,0)
    nuevo_cuerpo.speed(0)
    cuerpo.append(nuevo_cuerpo)
    
    marcador += 10
    if marcador > marcador_alto : 
      marcador_alto = marcador
      texto.clear()
      texto.write("marcado: {} Marcador más alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))
    
  total = len(cuerpo)
  for i in range(total -1,0,-1):
    x = cuerpo[i-1].xcor()
    y = cuerpo[i-1].ycor()
    cuerpo[i].goto(x,y)

  if total > 0 :
    x = snake.xcor()
    y = snake.ycor()
    cuerpo[0].goto(x,y)
  
  moviento()
  
  for i in cuerpo:
    if i.distance(snake)< 10:
      for i in cuerpo:
        i.clear()
        i.hideturtle()
      snake.home()
      cuerpo.clear()
      snake.direction = 'stop'
      marcador=0
      texto.clear()
      texto.write("marcado: {} Marcador más alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))
  
  
  time.sleep(retraso)#genera un dilay para que no se mueva tan tapido
  

turtle.done()