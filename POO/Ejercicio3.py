# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
class Fabrica:
  def __init__(self, llantas, color, precio):
    self.llantas = llantas
    self.color = color
    self.precio = precio
    
class Moto(Fabrica):
  def cantLlantas(self):
    return self.llantas
  
  def __str__(self):
      return """
          LLANTAS\t\t{}
          COLOR\t{}
          PRECIO\t{}""".format(self.llantas,self.color,self.precio)

class Carro(Fabrica):
  def cantLlantas(self):
    return self.llantas
  
  def __str__(self):
      return """
          LLANTAS\t\t{}
          COLOR\t{}
          PRECIO\t{}""".format(self.llantas,self.color,self.precio)
  
motito = Moto(2, "rojo", 2000)
print(motito)
print(motito.cantLlantas())

auto = Carro(4, "negro", 40000)
print(auto)
print(auto.cantLlantas())