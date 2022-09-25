# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Realizar un bucle "while" cuya condición de continuidad
# sea que <x sea menor a 10> y que <x sea distinto de 6>
# Colocar ambas condiciones como condicion del "while" realizando
# una condición compuesta (utilice el operador "and" o "or" según corresponda)
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

#Ejercicio 1

print("Inicio del primer ejercicio")

while x < 10 and x != 6:                #Son las dos codiciones solicitadas
    print("El valor de x es", x)        #Imprimo el valor de x antes de incremenetarlo
    x += 2                              #Realizo el incremento de a 2 por cada iteración

print("Primer ejercicio de while resuelto")

# Realice el mismo bucle "while" pero en vez de estar formado por una condición
# compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
# "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

#Ejercicio 2

print("Inicio del segundo ejercicio")

x = 0               #Vuelvo a definir x para que inicie desde 0. Podría poner otra variable en lugar de x
while x < 10:       #Condición solicitada
    if x == 6:      #Pregunto si el número es igual a 6
        break       #Si se cumple la condición, realizó una interrupción del bucle
    else:
        print("El valor de x es", x)        #Imprimo el valor de x antes de incrementar
        x += 2                              #Incremento el valor de x

print("Segundo ejercicio de while resuelto")
    

print("terminamos!")