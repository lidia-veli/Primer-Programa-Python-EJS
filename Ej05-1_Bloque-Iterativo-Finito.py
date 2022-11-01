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
    #esto va a meternos directamente en el bucle iterativo, que nos pedirá introducir de nuevo un número entre el 1 y el 10

# Mientras el número no esté entre 1 y 10
while not 1 <= numero <= 10: #ENTRAMOS EN EL BUCLE FINITO
    #El número no es válido
    #y le volvemos a pedir al usuario que introduzca un número
    numero = input("Introduzca otra vez un número entre 1 y 10: ")
    try:
        numero = int(numero)
    except:
        numero = 0

# Si el número introducido está entre 1 y 10:   
print("Estamos seguros de que el número introducido ", numero, "está comprendido entre 1 y 10 incluidos")


#COMENTARIO:
#El bucle no tendría por qué llegar a ejecutarse, si a la primera introducimos un número entre 1 y 10.
#Por eso los bucles finitos pueden se dice que pueden repetirse entre 0 y n veces.
#
#FORMA DE USO:
#Lo que estamos haciendo es crear un bucle finito con las condiciones opuestas a las que queremos verificar.
#De tal forma que, si no se están dando las condiciones que queremos, se repite el experimento hasta que se cumplen.
#Una vez se cumplen, se continúa con el código.

