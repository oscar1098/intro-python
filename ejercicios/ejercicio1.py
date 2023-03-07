'''
Crea un programa que pida dos números por teclado. El programa tendrá una función
llamada “DevuelveMax” encargada de devolver el número más alto de los dos
introducidos.
'''
num_mayor = 0
def devuelMax( num1,num2 ):
    if num1 != num2 and num1 > num2:
        num_mayor = num1
    else:
        num_mayor = num2
    return num_mayor

num1 = float(input('Digite el primer numero'))
num2 = float(input('Digite el segundo numero'))
print('El numero mayor es', devuelMax( num1,num2 ))