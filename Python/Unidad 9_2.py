from functools import reduce

def numeros(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

lista_numeros = list(range(100))

numeros(lista_numeros)