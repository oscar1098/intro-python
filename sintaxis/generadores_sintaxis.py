def generador(limite):
    
    num = 1
       
    while num < limite:

        yield num*2
        
        num = num +1

numPar = generador(10)

print(next(numPar))
print(next(numPar))

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelve_ciudades('Madrid','Barcelona','Bilbao','Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
