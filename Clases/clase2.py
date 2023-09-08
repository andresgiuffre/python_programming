# FUNCIONES DE ORDEN SUPERIOR


def sumar(x):
    return x + 10

def cuadrado(x):
    return x ** 2

def superior(funcion, lista):
    resultado = []
    for num in lista:
        resultado.append(funcion(num))
    return resultado

numeros = [2, 5, 10]
#print(superior(sumar, numeros))
#print(superior(cuadrado, numeros))


# FUNCIONES LAMBDA

lambda x : x + 10
lambda x : x ** 2

#print(superior(lambda x : x + 10, numeros))
#print(superior(lambda x : x ** 2, numeros))


# EXCEPCIONES

try:
    int('1')
except (ValueError, Exception):
    print("El argumento no es un número")
except NameError:
    print("Ese no es el nombre")
except TabError:
    print("No es el tab")
else:
    print("Todo salió bien")
finally:
    print("Se terminó el bloque")

