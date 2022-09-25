# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
cantidad_numeros_negativos = 0  # Inicializo el contador en 0 de los números negativos

# for ... in range(....)

for x in range(inicio,fin+1):               #Bucle for para recorrer la secuencia: fin+1 para que tome el valor de fin ingresado
    if x >= 0:
        cantidad_numeros_positivos += 1     #Cuento los números positivos
    else:
        cantidad_numeros_negativos += 1     #Cuento los números negativos

# Imprimir el valor de la cantidad de números positivos y negativos

print("La cantidad de números positivos en el rango ingresado es (con el 0 incluido)")
print(cantidad_numeros_positivos)
print("La cantidad de números negativos es")
print(cantidad_numeros_negativos)

print("Ejercicio resuelto")

print("terminamos!")
