'''
El centro de investigacion sismologica en colombia desea crear un alogirtmo que permita llevar el registro promedio de movimientos teluricos ocurridos en 6 diferentes ciudades del pais. El algoritmo debe permitir ek ingreso del nombre de cada ciudad y por cada ciudad se debe registrar un muestreo de 10 movimientos. El centro de investigacion requiere que el algoritmo cumpla con los siguientes requisitos:

1) Los nombres de las ciudades se deben guardar en un arreglo
2) El algoritmo debe permitir calcular el promedio de los movimientos teluricos y guardarlos en un arreglo
3) El algoritmo debe mostrar las ciudades registradas y el promedio obtenido
4) El alogoritmo debe mostrar el nombre de la ciudad que registro mayot promedio
'''

registro = []
op = 1
nro = 3

while op !=5:
    print('1. Registrar ciudad\n2. Ver datos\n3. Registrar movimientos teluricos\n4.Ver ciudad con mayor primedio\n5.Salir')
    op = int(input(':)_'))
    if ( op == 1):
        ciudad = input('Ingrese el nombre de la ciudad: ')
        codigo = input('Ingrese el codigo de la ciudad: ')
        registro.append([codigo,ciudad,0.0])
    elif (op == 2):
        print(f'Codigo\t\t ciudad\t\t promedio\t\t')
        for i in registro:
            print(f'{i[0]}\t\t {i[1]}\t\t {i[2]}')
        x = input('Press any key....')
    elif (op == 3):
        print(f'Codigo\t\t ciudad\t\t promedio\t\t')
        for i in registro:
            print(f'{i[0]}\t\t {i[1]}\t\t {i[2]}')
        codbu = input('Ingrese el codigo de la ciudad ')
        for i in registro:
            if codbu in i:
                suma = 0
                for j in range(0,nro,1):         
                    suma += float(input('Ingrese el movimiento telurico '))
                i[2] = suma/nro               
        x = input('Press any key....')
                    
    elif (op == 4):
        prom = 0
        indxciudad = 0
        for i,j in enumerate(registro):
            if (j[2] > prom):
                indxciudad = i
                prom = j[2]
        print(f'La ciudad con el mayor promedio es {registro[indxciudad][1]} con un promedio de {registro[indxciudad][2]}')

    elif (op == 5):
        print('Busca Refugio....')

    else:
        print('La opcion ingresada no es valida')
        x = input('Press any key...')