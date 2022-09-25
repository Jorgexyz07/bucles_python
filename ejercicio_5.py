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
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

# for ... in range(....)

for x in range(inicio,fin+1):           #Bucle for para recorrer la secuencia: fin+1 para que tome el valor de fin ingresado
    sumatoria += x                      #Calcula la sumatoria total de la secuencia
    
# Imprimir el valor de la sumatoria

print("La sumatoria total es", sumatoria)   #Imprimo el resultado de la sumatoria total de la secuencia

print("Ejercicio resuelto")

print("terminamos!")
