#EJERCICIO:
#Imaginemos que pedimos al usuario introducir un número comprendido entre 1 y 10, aunque esta vez, 
# le pedimos un valor en caso de error en lugar de salir del programa, # tantas veces como se equivoque.

#También se puede resolver usando un bloque finito:

while True: #entramos en un bucle infinito, esto es, se va a repetir siempre, a no ser que se den las condiciones que queramos
    #el usuario introduce un número
    numero = input("Introduzca un número entre 1 y 10: ")
    
    try: #intentamos trasnformarlo a entero
        numero = int(numero) #si se puede, se asigna a la variable numero
    except:
        pass #si no se puede, se repite el bucle

    #una vez tenemos el entero
    else: #establecemos la condición necesaria para salir del bucle infinito
        if 1 <= numero <= 10:
            #si el número está entre 1 y 10, salimos del bucle
            break #INDICADOR SALIR BUCLE INFINITO

#si hemos conseguido salir del bucle es poruq el numero introducido está entre el 1 y el 10, por lo tanto:
print("El número",numero,"está comprendido entre el 1 y el 10 incluidos")
