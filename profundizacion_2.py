# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:
    numero_1 = float(input("Ingrese un número\n"))      #Solicito los dos números y la operación que se desa realizar
    numero_2 = float(input("Ingrese otro número\n"))
    operacion = str(input("Ingrese la operación que desea realizar: suma +, resta -, multiplicación *, división /. Para salir ingrese FIN\n"))
    if operacion == "+":   
        suma = float(numero_1 + numero_2) 
        print("La operación solicitada es la suma. El resultado de esta operación es", suma)                            #Verifico que operación se solicitoó
    elif operacion == "-":
        resta = float(numero_1 - numero_2)
        print("La operación solicitada es la resta. El resultado de esta operación es", resta) 
    elif operacion == "*":
        multiplicacion = float(numero_1 * numero_2)
        print("La operación solicitada es la multiplicación. El resultado de esta operación es", multiplicacion) 
    elif operacion == "/":
        division = float(numero_1 / numero_2)
        print("La operación solicitada es la división. El resultado de esta operación es", division) 
    elif operacion == "FIN":
        break
    else:
        print("Ingrese un operación válida")

print("Ejercicio de profundización 2 realizado")