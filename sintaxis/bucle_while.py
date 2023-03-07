import math

edad = int(input('Introduce la edad '))

while edad < 0:
    print('Edad incorrecta')
    edad = int(input('Introduce la edad '))

print('Gracias por colaborar puedes pasar')
print('Edad del aspirante '+str(edad))

print('Programa de calculo de raiz cuadrada')
numero = int(input('Introduce un numero'))

intentos = 0

while numero < 0:
    print('No se puede hallar la raiz de un numero negativo')
    if intentos == 2:
        print('Has consumido deamasiados intentos. El programa a finzalizado')
        break;
    numero = int(input('Introduce un numero'))
    if numero < 0:
        intentos =+1

if intentos < 2:
    solucion = math.sqrt(numero)
    print('La razin cuadrada de ' + str(numero) + ' es ' + str(solucion))
        
