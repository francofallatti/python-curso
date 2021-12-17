# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
class Calculadora:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def sum(self):
    print(self.a + self.b)
  
  def res(self):
    print(self.a - self.b)
  
  def mul(self):
    print(self.a * self.b)

  def div(self):
    print(self.a / self.b)

# cal = Calculadora(2,3)
# cal.sum()
# cal.res()
# cal.div()
# cal.mul()

# Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentagono
class  Areas:
  def __init__(self, base, altura):
    self.base=base
    self.altura=altura
  
  def cuadrado(self):
    print(self.base * self.altura)
    
  def triangulo(self):
    print((self.base * self.altura)/2)
    
  def pentagono(self):
    print((5*self.base * self.altura)/2)
    

