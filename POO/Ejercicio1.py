import math
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno:
  def datos(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
  
  def imprimir(self):
    print("Nombre: ",self.nombre)
    print("Nota: ",self.nota)

  def aprobo(self):
    if self.nota <6:
      print("reprobó")
    else:
      print("aprobó")
      
      
# Escribir una clase en python que calcule pow(x, n)
# x = es la base
# n = es el exponente
class calcPow:
  def datos(self,x,n):
    self.x=x
    self.n=n
    
  def calc(self):
    return math.pow(self.x, self.n)
  
