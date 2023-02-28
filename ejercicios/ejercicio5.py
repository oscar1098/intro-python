'''
Crea un programa que pida por teclado introducir una contraseña. La contraseña no
podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
errónea”
'''

contraseña = input('Ingrese la contraseña')
nro_caracteres = int(len(contraseña))
print(nro_caracteres)
count = 0

for i in contraseña:
    if i == ' ':
        count +=1

if nro_caracteres < 8 or count !=0:
    print('Ingrese una contraseña valida')
else:
    print('Contraseña valida')

