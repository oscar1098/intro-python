'''
Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducidos
'''

contador = 0
x = float(input('Ingrese un numero positivo'))
while x > 0:
    contador = x + contador
    x = float(input('Ingrese un numero positivo'))

print(contador)