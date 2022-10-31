#Muestre la suma de los dos números además de la comparación y compruebe que todo va bien esta vez.

#Pedimos al usuario que introduzca dos números
numero1 = input("Introduzca un primer número: ")
numero1 = int(numero1) #convertimos el string a entero

numero2 = input("Introduzca un segundo número: ")
numero2 = int(numero2) #entero

#Comparamos los números
comparacion = numero1 < numero2
#Hacemos la suma
suma = numero1 + numero2

#Mostramos el resultado
print( numero1,"<",numero2,"es",comparacion)
print( numero1,"+",numero2,"es",suma)
