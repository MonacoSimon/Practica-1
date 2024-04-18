#Clase  persona, atributos = nombre y edad, metodo: get y seter,mostrar los los datos y decir si es mayor de edad

class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad

    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_edad(self,edad):
        self.edad = edad




persona1 = Persona("nombre","11")
nombre = persona1.get_nombre
edad = persona1.get_edad
if persona1.edad >= "18":
    print(f"La persona {persona1.nombre} es Mayor de edad ")
elif persona1.edad <= "18":
    print("La persona es menor de edad")



     