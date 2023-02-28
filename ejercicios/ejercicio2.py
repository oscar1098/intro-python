'''
Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
teclado).
'''

lista =[]
lista.append(input('Digite su nombre '))
lista.append(input('Digite su Direccion '))
lista.append(input('Digite su Telefono '))

print('Su Nombre es: ', lista[0])
print('Su DireccionS es: ', lista[1])
print('Su Telefono es: ', lista[2])
print('Los datos personale son ', lista[0], ' ', lista[1], ' ', lista[2] )