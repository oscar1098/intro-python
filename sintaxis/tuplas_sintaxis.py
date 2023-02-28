 #? Es una lista inmutable
nombreTupla = ('elem1','elem2','elem3','elem1')
print(nombreTupla)

 #? Acceder a un elemento
print(nombreTupla[1])

 #? convertir tupla a lista
miLista = list(nombreTupla)
print(miLista)

 #? convertir lista a tupla
miTupla = tuple(miLista)
print(miTupla)

 #? cuantos veces se encuentra un elemento en la tupla
print(miTupla.count('elem1'))

 #? Longitud de una tupla
print(len(miTupla))
