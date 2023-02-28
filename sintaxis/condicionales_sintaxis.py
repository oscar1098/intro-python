 #? switch
menu = '''
Menu 
1. Mostrar numero
2. Mostrar texto
3. Mostrar signo
4. Imprimir opcion
'''
print(menu)
op = int(input('selecciona un caso'))
if op is 1:
    variable = input('Digita tu numero')
    print(variable)
elif op is 2:
    variable = input('Digita el texto')
    print(variable)
elif op is 3:
    variable = input('Digita el signo')
    print(variable)
else:
    print('Tecla incorrecta seleccione (1,2,3)')
