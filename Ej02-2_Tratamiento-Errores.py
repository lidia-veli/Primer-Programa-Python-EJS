#Nuestra solución alternativa consiste en decir que si no puede convertirse alguno de los números, 
# se muestre un mensaje de error y a continuación, se salga del programa. 
#El usuario tendrá que volver a ejecutarlo e introducir de nuevo los datos, si lo desea.


#importar módulo sys
import sys
    #sys.exit() es una función que permite salir del programa
    #sys.stderr devuelve un objeto de tipo file que se puede usar para escribir mensajes de error


#Tratamos la primera excepción
numero1 = input("Introduzca un primer número: ")

try: #SECCIÓN CRÍTICA
    numero1 = int(numero1) #intentamos convertir el número a entero

except: #SECCIÓN DE TRATAMIENTO DE EXCEPCIONES: que se ejecuta si se da alguna excepción en la sección crítica
    print("Error: La conversión de este número no es posible", file=sys.stderr)
    sys.exit() #salimos del programa


#Tratamos la segunda excepción
numero2 = input("Introduzca un segundo número: ")

try: 
    numero2 = int(numero2) 

except ValueError as e: #sólo se capturan las excepciones de tipo ValueError, producidas por la conversión a entero
    print("La conversión de este número no es posible", file=sys.stderr) 
    sys.exit()


#Comparamos los números
comparacion = numero1 < numero2
#Hacemos la suma
suma = numero1 + numero2

#Mostramos el resultado
print( numero1,"<",numero2,"es",comparacion)
print( numero1,"+",numero2,"es",suma)
