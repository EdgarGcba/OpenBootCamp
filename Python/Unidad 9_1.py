pais = ""
pais_list = []
while pais != 'f':
    pais = input ("Ingrese el nombre de un pais: (f para terminar) ")
    if pais != 'f':
        pais_list.append(pais)
print(list(pais_list))
pais_set = pais_list
pais_set_ordenado = sorted(pais_set)
print(set(pais_set))
        
    
