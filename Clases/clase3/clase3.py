# CLASES Y OBJETOS

"""
class MiClase:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def imprimir_edad(self):
        print(self.edad)


mi_objeto = MiClase("Juan", 34)
mi_objeto.imprimir_edad()
"""

"""
class OperacionesMatematicas:
    def __init__(self, numero):
        self.numero = numero


    def sumar(self, nro2):
        self.numero += nro2
        print(self.numero)


    def restar(self, nro2):
        self.numero -= nro2
        print(self.numero)


    def multiplicar(self, nro2):
        self.numero *= nro2
        print(self.numero)


mi_objeto = OperacionesMatematicas(10)
mi_objeto.sumar(5)
mi_objeto.restar(4)
mi_objeto.multiplicar(2)
mi_objeto.sumar(3)

otro_objeto = OperacionesMatematicas(3)
otro_objeto.sumar(8)
"""

# ENCAPSULAMIENTO

# Getters, Setters y Del

"""
class Clase:
    def __init__(self):
        self.__atributo = "Atributo Oculto"

    
    def get_atributo(self): # Getter
        return self.__atributo
    

    def set_atributo(self, valor): # Setter
        self.__atributo = valor


    def eliminar_atributo(self): # Del
        del self.__atributo


    def __saludo_privado(self):
        print("Hola!!, este es un saludo privado")


    def saludo_publico(self):
        self.__saludo_privado()
"""

# HERENCIA

# La clase Base, padre o superclase que contiene métodos y atributos que otras clases van a heredar
# La clase Derivada, hija o subclase que va a hereder métodos y atributos del padre.

"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas


class ClaseA:
    def __init__(self):
        self.a = 1

    def mensaje(self):
        print("Mensaje de la Clase A")


class ClaseB:
    def __init__(self):
        self.a = 2

    def mensaje(self):
        print("Mensaje de la clase B")


class ClaseC(ClaseA, ClaseB):
    def mensaje(self):
        print("Mensaje clase C") # Sobreescritura
        super().mensaje()


mi_objeto = ClaseC()
mi_objeto.mensaje()
"""

# POLIMORFISMO

"""
class Perro:
    def sonido(self):
        return "Guau!"
    

class Gato:
    def sonido(self):
        return "Miau!"
    

def sonido_del_animal(animal):
    return animal.sonido()

perro = Perro()
gato = Gato()

print(sonido_del_animal(perro))
print(sonido_del_animal(gato))
"""

"""
import math

class Figura:
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio


    def calcular_area(self):
        return math.pi * self.radio ** 2
    

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        return self.base * self.altura
    

# Creo las instancias de las subclases
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Calcular el área de diferentes figuras usando polimorfismo
def calcular_y_mostrar_area(figura):
    area = figura.calcular_area()
    print(f"El área de la figura es: {area}")


calcular_y_mostrar_area(circulo)
calcular_y_mostrar_area(rectangulo)
"""
