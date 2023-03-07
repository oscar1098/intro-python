'''
Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior.
'''
num1 = int(input('Ingrese el numero un numero '))
num2 = int(input('Ingrese un numero mayor que ' + str(num1) + ': '))

while num2 > num1:
    num1 = num2
    num2 = int(input('Ingrese un numero mayor que '+ str(num1) + ': '))

print(num2, ' no es mayor que ', num1)



