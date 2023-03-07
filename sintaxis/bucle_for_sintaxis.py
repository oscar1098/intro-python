for i in [1,2,3]:
    print('i')    

for i in ['hola','mundo','python']:
    print(i)    

for i in ['elemento 1','elemento 2',3]:
    print('hola ', end = '') #No hace salto de linea en la impresion

for i in range(5,50,5):
    print(i)

valido = False

email = input('Introduc tu email')

for i in range(len(email)):
    if email[i] == '@':
        valido = True 

if valido:
    print('Email correcto')
else:
    print('Correo invalido')