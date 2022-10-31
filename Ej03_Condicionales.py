#EJ 3: Ejercicio: Modifique estas condiciones para hacerlas exclusivas 
# y haga que el bloque else se ejecute en caso de igualdad entre ambos números.

#Pedemos al usuario que ingrese dos números
numero1 = int(input("Inserte un número: "))
numero2 = int(input("Inserte otro número: "))

#Comparamos los números
if numero1 < numero2: #Si n1 es menor que n2
    print(numero1, "es menor que", numero2)

elif numero1 > numero2: #si no, si n1 es mayor que n2
    print(numero1, "es mayor que", numero2)

else: #si no se dan ninguna de las dos condiciones anteriores (si no es menor, ni mayor), entonces son iguales
    print(numero1, "es igual a", numero2)
