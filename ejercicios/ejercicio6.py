'''
Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
correcta si solo tiene una “@” y si tiene uno o más “.”
'''

contPunto = 0;
contArroba = 0;

correo = input('Ingrese la direccion de correo electronico ')

for i in correo:
    if i == '@':
        contArroba +=1
    if i == '.':
        contPunto +=1

if contArroba == 1 and contPunto >= 1:
    print('Direccion de correo valida')
else:
    print('Direccion de correo invalida')

