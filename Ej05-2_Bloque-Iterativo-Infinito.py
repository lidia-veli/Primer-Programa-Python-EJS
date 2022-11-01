#EJERCICIO:
#Imaginemos que pedimos al usuario introducir un número comprendido entre 1 y 10, aunque esta vez, 
# le pedimos un valor en caso de error en lugar de salir del programa, # tantas veces como se equivoque.

#LO VAMOS A RESOLVER USANDO UN BUCLE ITERATIVO INFINITO

while True: #ENTRAMOS EN UN BUCLE INFINITO
            #esto es, se va a repetir siempre, a no ser que se den unas condiciones
    #el usuario introduce un número
    numero = input("Introduzca un número entre 1 y 10: ")
    
    try: #intentamos trasnformarlo a entero
        numero = int(numero) #si se puede, se asigna a la variable numero
    except:
        pass #si no se puede convertir, se repite el bucle

    #una vez tenemos el entero
    else: #establecemos la CONDICIÓN NECESARIA PARA SALIR DEL BUCLE INFINITO
        if 1 <= numero <= 10:
            #si el número está entre 1 y 10, salimos del bucle
            break #INDICADOR SALIR BUCLE INFINITO

#si hemos conseguido salir del bucle es porque el numero introducido está entre el 1 y el 10, por lo tanto:
print("El número",numero,"está comprendido entre el 1 y el 10 incluidos")


#COMENTARIO:
#Lo que estamos haciendo es crear un bucle infinito de pedir al usuario y número entre el 1 y el 10, 
# del que sólo podremos salir si se cumple la condición de que el número es un entero y está entre el 1 y el 10.
# Por lo tanto, el resto del código sólo se podrá ejecutar una vez hayamos cumplido dichas condiciones.

#FORMA DE USO: 
# nuestra forma de asegurarnos de que se cumplen unas condiciones es si el código posterior al bucle se ejecuta.
# Esto se da, sólo si se han cumplido las condiciones establecidas en el 'else:' (nuestras condiciones).

