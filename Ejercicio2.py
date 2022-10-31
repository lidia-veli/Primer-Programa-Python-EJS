#Simule un error de entrada escribiendo letras o no escribiendo nada y pulsando la tecla [Intro]. ¿Qué ocurre?

#Pedimos al usuario que introduzca dos números (transformamos los inputs de string a entero)
numero1 = int(input("Introduzca un primer número: "))
numero2 = int(input("Introduzca un segundo número: "))

#Comparamos los números
comparacion = numero1 < numero2
#Hacemos la suma
suma = numero1 + numero2

#Mostramos el resultado
print( numero1,"<",numero2,"es",comparacion)
print( numero1,"+",numero2,"es",suma)

#OUTPUT:
#si escribimos letras o no escribimos nada y pulsamos la tecla [Intro] nos da un error de tipo ValueError
    #ValueError: invalid literal for int() with base 10: 'hola'
    #ValueError: invalid literal for int() with base 10: ''
