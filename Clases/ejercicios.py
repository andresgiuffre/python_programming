"""
lista=[1,2,3,4,5,6,7,8,9,50]
cont=0
suma=0
while cont<=len(lista)-2:
    suma=suma+lista[cont]
    cont+=1

print(suma)
"""
"""
lista = [10, 2, 5, 8, 7]

suma = 0

for num in lista[:-1]:
    suma += num

print("La suma de los números excepto el último es:", suma)
"""
"""
lista=[1,2,3,4,5,6,7,8,9,50]

nul=[]
while nul!=lista:
    print(lista[-1])

    lista.remove(lista[-1])

print(lista)
"""

"""
lista = [1, 2, 3, 4, 5]


while lista:
    
    print(lista[0])
    
    del lista[0]

print(lista)
"""