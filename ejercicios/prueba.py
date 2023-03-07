'''
El centro de entrenamiento Campus desea llevar el registro de todos los participantes en el programa de entrenamiento; el comite academico le solicita organizar los diferentes grupos por categoria (basico,intermedio, avanzado). El programa debe permitir registrar los candidatos y almacenarlos en una lista, la informacion de los candidatos es la siguiente:
    -Nombre
    -id de identificacion
    -Edad
    -Genero
    -Nivel de estudio(Bachiller, profesional,universitario,independiente)
El comite academico tiene dispuesto para los candidatos una prueba que busca medir sus conociemientos en el area de programacion para tal fin evaluara las tematicas de fundamentos de programacion,html,css, bases de datos y github. Cada uno de estos tres ejes tematicos tienen un valor minimo de 1.0 y maximo de 5.0. El programa debe permitir almacenar las calificaciones de los candidatos para asi ordenar los candidatos de acuerdo a la categoria. El programa debe contener el siguiente menu de opciones:
    1.Registro de candidatos
    2.Registro de notas por candidato: El programa debe permitir buscar el candidato en la lista de postulaciones para verificar que la persona se encuentra registrada, si la persona se encuentra registrada se debe solicitar las notas obtenidas en cada uno de los ejes tematicos evaluados(fundamentos de programacion, html, css, bases de datos y github)
    3.Clasificacion: El programa debe permitir organizar de forma automata cada uno de los participantes de acuerdo al promedio obtenido en cada una de las pruebas.
     Tenga en cuenta la siguiente tabla de clasificacion:
        a. Si el puntaje esta entre 3.0 y 3.5 se asignara a grupo basico
        b. Si el promedio es mayor igual que 3.5 y menor a 4.0 es intermedio
        c. Si el promedio es mayor igual a 4.0 y menor a 5.0 es avanzado
     La clasificacion de los grupos se debe hacer de forma automatica de acuerdo al puntaje obtenido. Puede crear una lista para cada categoria si asi lo prefiere.
    4. Listar las personas que quedaron en basico
    5. Listar las personas que quedaron en intermedio
    6. listar las personas que quedaron en avanzado
    7. Clasificar reprobados: Almacenar en una lista aquellos candidatos que no superaron la prueba
    8. Listar reprobados
'''

candidatos = []
basicoF = []
intermedioF = []
avanzadoF = []
reprobadoF= []
basicoH = []
intermedioH = []
avanzadoH = []
reprobadoH= []
basicoC = []
intermedioC = []
avanzadoC = []
reprobadoC= []
basicoB = []
intermedioB = []
avanzadoB = []
reprobadoB= []
basicoG = []
intermedioG = []
avanzadoG = []
reprobadoG= []
op = True 

while op:
    print('1.Ingresar un candidato\n2.Ingresar notas\n3.clasificar estudiantes\n4.Lista de candidatos en basico\n5.Lista de candidatos en intermedio\n6.Lista de candidatos en avanzado\n7.Lista de reprobados\n8.Ver candidatos\n9.Salir')
    menu = int(input(':)_'))
    if (menu == 1):

        nombre = input('Ingrese el nombre del candidato: ')
        id = input('Ingrese la identificacion del candidato: ')
        edad = input('Ingrese la edad del candidato: ')
        genero = input('Ingrese el genero del candidato: ')
        estudio = int(input('Ingrese el nivel de estudio del candidato (1-Bachiller, 2-profesional, 3-universitario independiente: )'))
        y = True
        while y:
            if (estudio == 1):
                estudio = 'Bachiller'
                y = False
            elif (estudio == 2):
                estudio = 'Profesional'
                y = False
            elif (estudio == 3):
                estudio = 'universitario independiente'
                y = False
            else: 
                estudio = int(input('Ingrese solo 1, 2 o 3 '))
                
        candidatos.append([nombre,id,edad,genero,estudio,[],[],[],[],[]])
        x = input('Presione cualquier tecla para volver al menu ')
    
    if (menu == 2):

        validarId = input('ingrese el numero de identificacion ')
        for i in candidatos:
            if validarId == i[1]:
                y = True
                while y:
                    print('1.para fundamentos\n2.para html\n3.para css\n4.bases de datos\n5.github\n6.salir')
                    nota =int(input(':)_ ')) 
                    def notas (indice):
                        fundame = float(input('Ingrese la nota '))
                        i[indice].append(fundame)
                        x = True
                        while x:
                            validar = int(input('1-Ingresar nueva nota, 2-volver al menu notas '))
                            if validar == 1:
                                fundame = float(input('Ingrese la nota '))
                                i[indice].append(fundame)
                            elif validar == 2:
                                x = False
                            else:
                                print('Ingrese solo 1 o 2')

                    if nota == 1:
                        notas(5)
                        
                    if nota == 2:
                        notas(6)
                        
                    if nota == 3:
                        notas(7)
                        
                    if nota == 4:
                        notas(8)
                        
                    if nota == 5:
                        notas(9)
                        
                    if nota == 6:
                        y = False
                    
    if(menu == 3):
        def enlistar(indice,lista1,lista2,lista3,lista4):
            for k,i in enumerate(candidatos):
                suma = 0
                for j in i[indice]:
                    suma += j
                prom = suma/len(i[indice])
                if (prom < 3.5 and prom >= 3.0) : 
                    lista1.append([candidatos[k][0],candidatos[k][1],candidatos[k][indice]])
                elif (prom < 4.0 and prom >= 3.5):
                    lista2.append([candidatos[k][0],candidatos[k][1],candidatos[k][indice]])
                elif (prom < 5.0 and prom >= 4.0):
                    lista3.append([candidatos[k][0],candidatos[k][1],candidatos[k][indice]])
                elif (prom < 3.0):
                    lista4.append([candidatos[k][0],candidatos[k][1],candidatos[k][indice]])
                
        # ? Listas de fundamentos
        enlistar(5,basicoF,intermedioF,avanzadoF,reprobadoF)
        # ? Listas de html
        enlistar(6,basicoH,intermedioH,avanzadoH,reprobadoH)
        # ? Listas de css
        enlistar(7,basicoC,intermedioC,avanzadoC,reprobadoC)
        # ? Listas de bases de datos
        enlistar(8,basicoB,intermedioB,avanzadoB,reprobadoB)
        # ? Listas de github
        enlistar(9,basicoG,intermedioG,avanzadoG,reprobadoG)

        print('Clasificacion exitosa')
        x = input('Presione cualquier tecla para volver al menu ')

    def mostrar(nombre,lista1,lista2,lista3,lista4,lista5):
        x = True
        while x:
            print(f'1.Candidatos {nombre} en fundamentos\n2.Candidatos {nombre} en html\n3.Candidatos {nombre} en css\n4.Candidatos {nombre} en Bases de datos\n5.Candidatos {nombre} en github\n6.Salir')
            y = int(input(':)_'))
            if (y==1):
                print(lista1)
            if (y==2):
                print(lista2)
            if (y==3):
                print(lista3)
            if (y==4):
                print(lista4)
            if (y==5):
                print(lista5)
            if (y==6):
                x = False

    if (menu == 4):
        mostrar('basico',basicoF,basicoH,basicoC,basicoB,basicoG)

    if (menu == 5):
        mostrar('intermedio',intermedioF,intermedioH,intermedioC,intermedioB,intermedioG)

    if (menu == 6):
        mostrar('avanzado',avanzadoF,avanzadoH,avanzadoC,avanzadoB,avanzadoG)
    if (menu == 7):
        mostrar('reprobado',reprobadoF,reprobadoH,reprobadoC,reprobadoB,reprobadoG)
    
    if (menu == 8):
        print(candidatos)
    if (menu == 9):
        op = False
