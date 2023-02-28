 #? Crear diccionario - mapa
midiccionario = {'Alemania':'Berlin','Francia':'Paris','Reino Unido':'Londres','España':'Madrid'}
print(midiccionario)

 #? Acceder a un elemento del diccionario
print(midiccionario['Francia'])

 #? Agregar elementos a un diccionario
midiccionario['italia']='Lisboa'
print(midiccionario)

 #? Modificar el valor de un elemento
midiccionario['italia'] = 'Roma'
print(midiccionario)

 #? Elminar elemento
del midiccionario['España']
print(midiccionario)

 #? Asignar valor a cada elemento de una lista
miLista = ['España','Francia','Reino Unido', 'Alemania']
midiccionario = {miLista[0]:'Madrid',miLista[1]:'Paris',miLista[2]:'Reino Unido',miLista[3]:'Berlin'}
print(miLista)
print(midiccionario)

 #? Asignar una lista a un elemento en un diccionario
midiccionario = {23:'Jordan','Nombre':'Michae','Equipo':'Chicago','Anillos':[1991,1992,1993,1996,1997,1998]}
print(midiccionario)

 #? Asignar un diccionario a un elemento del diccionario
midiccionario = {23:'Jordan','Nombre':'Michael','Equipo':'Chicago','Anillos':{'temporadas':[1991,1992,1993,1996,1997,1998]}}
print(midiccionario)

print(midiccionario['Anillos']['temporadas'][4])

 #? Metodos
print(midiccionario.keys()) # Muestra las claves del diccionario
print(midiccionario.values()) # Mustra los valores del diccionario
print(len(midiccionario))

print(len(midiccionario['Anillos']))