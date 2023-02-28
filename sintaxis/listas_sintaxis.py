 #? Sintaxis de las listas
'''
nombreLista = [elem1,elem2,elem3...]
'''

 #? Declarar una lista
miLista = ['Maria','Marta','Marcos','Antonio']
print( miLista )
print( miLista[2] )
 #*Cuando se coloca un indice negativo empieza desde el final empezandp en 1
print( miLista[-3] )

 #? Acceder a una porcion de una lista incluye el indice 0, excluye el indice 3
print( miLista[0:3] )

 #? Agregar elemento al final de la lisa
miLista.append('Sandra')

 #? Agregar en una ubicacion de la lista de la lista
miLista.insert( 0, 'Pablo' )
print(miLista)

 #? Agregar varios elementos a la lista
miLista.extend(['Miel','Rafael','Naco'])

 #? Indice de un elemento (pueden haber varios elementos iguales, toma el primero)
print(miLista.index('Marcos'))

 #? Verificar que un elemento este dentro de la lista
print('Miel' in miLista )
print(miLista)

 #? Eliminar elementos
miLista.remove('Miel')
print(miLista)

 #? Eliminar ultimo elemento de una lista
miLista.pop()

 #? Unir dos listas
miLista2 = ['Daniel',12,34,10]
miLista3 = miLista + miLista2
print(miLista3)

 #? repetir la lista 
print(miLista3*3)