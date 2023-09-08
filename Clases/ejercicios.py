"""
lista = [0, 1]

def fibo(num):
    if num <= 2:
        print("El numero debe ser mayor a 2")
    else:
        for i in range(2, num):
            lista.append(lista[i-2] + lista[i-1])
    return lista


print(fibo(2))
"""

def fibo(n):
    if n <= 2:
        return "El número debe ser mayor que 2."
        
    fibonacci = [0, 1]
    
    while len(fibonacci) < n:
        next = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next)
    
    return fibonacci

prueba = 2
resultado = fibo(prueba)
print(resultado)