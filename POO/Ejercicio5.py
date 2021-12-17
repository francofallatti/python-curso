# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad:
  def __init__(self, nombreU):
    self.nombreU = nombreU
    
class Carrera:
  def carrera(self, especialidad) :
      self.especialidad = especialidad
      
class Estudiante(Universidad,Carrera):
  def datos(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def __str__(self):
      return """
          Nombre\t\t{}
          Edad\t{}
          Universidad\t{}
          Carrera\t{}""".format(self.nombre,self.edad,self.nombreU,self.especialidad)
    
persona = Estudiante("UBA")
persona.carrera("Sistemas")
persona.datos("Juan", 20)

print(persona)