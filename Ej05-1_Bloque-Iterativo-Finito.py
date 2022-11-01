#Esta vez, no se trata de determinar si hay que ejecutar o no un bloque, sino de determinar si hay que repetirlo. 
# Este bloque podrá repetirse de 0 a n veces.
#
#EJERCICIO:
#Imaginemos que pedimos al usuario introducir un número comprendido entre 1 y 10, aunque esta vez, 
# le pedimos un valor en caso de error en lugar de salir del programa, # tantas veces como se equivoque.

#LO VAMOS A RESOLVER USANDO UN BUCLE ITERATIVO FINITO

#Pedimos al usuario que introduzca un número
numero = input("Introduzca un número entre 1 y 10: ")
try:
    numero = int(numero)
except:
    numero = 0 #si no se puede convertir a entero, se le asigna el valor 0
    #esto va a hacer que numero no cumpla la condición del bucle, y se siga pidiendo al usuario que introduzca un número entre 1 y 10

#Mientras el número no esté entre 1 y 10
while not 1 <= numero <= 10:
    #El número no es válido
    #y le volvemos a pedir al usuario que introduzca un número
    numero = input("Introduzca otra vez un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        numero = 0
    
print("Estamos seguros de que el número introducido ", numero, "está comprendido entre 1 y 10 incluidos")


