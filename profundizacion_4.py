# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
En este ejercicio se lo provee de una lista de temperaturas,
esa lista de temperaturas corresponde a los valores de temperaturas
tomados durante una temporada del año en Buenos Aires.
Usted deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperaturas

Los resultados se deberán almacenar en las variables
que ya hemos preparado para usted al comienzo del ejercicio

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase/ejemplo_5.py)
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......

for x in temp_dataloger:            #Recorro la lista
    temperatura_sumatoria += x      #Sumo las temperaturas
    temperatura_len += 1            #Contabilizo la cantidad de temperaturas
    if (temperatura_max is None) or (x > temperatura_max):          #Busco la temperatura máxima
        temperatura_max = x
    elif (temperatura_min is None) or (x < temperatura_min):        #Busco la temperatura mínima
        temperatura_min = x
    else:
        pass
print("La temperatura máxima es:", temperatura_max)

print("La temperatura mínima es:", temperatura_min)

# Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp

#Verifico si los valores de temperatura máx y mín son iguales a los hallados con la función
maxima = max(temp_dataloger)
minima = min(temp_dataloger)

if maxima == temperatura_max and minima == temperatura_min:
    print("Las temperaturas máx y mín son iguales a las calculadas con las funciones max y min")
    print("La temperatura máxima calculada es", temperatura_max, "y con la función es", maxima)
    print("La temperatura mínima calculada es", temperatura_min, "y con la función es", minima)
else:
    print("Las temperaturas máx y mín no son iguales a las calculadas con las funciones max y min")

# Al finalizar el bucle debe calcular el promedio como:
# temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

temperatura_promedio = temperatura_sumatoria / temperatura_len

print("La temperatura promedio es:", temperatura_promedio,"°C")


# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

#Verifico si el resultado de la temperatura_sumatoria es igual al calculado con la función sum

suma = sum(temp_dataloger)

if suma == temperatura_sumatoria:
    print("La suma de las temperaturas calculadas es igual a la suma encontrada con la función")
    print("La suma de las temperaturas calculada es", temperatura_sumatoria, "y con la función es", suma)
else:
    print("La suma de las temperaturas calculadas no es igual a la suma encontrada con la función")

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo

#Defino la época del año 

if (temperatura_min >= 17 and temperatura_min <= 21) and (temperatura_max >= 26 and temperatura_max <= 30):
    print("Según las temperaturas registradas, nos encontramos en verano")
elif (temperatura_min >= 9 and temperatura_min <= 13) and (temperatura_max >= 18 and temperatura_max <= 22):
    print("Según las temperaturas registradas, nos encontramos en otoño")
elif (temperatura_min >= 6 and temperatura_min <= 10) and (temperatura_max >= 12 and temperatura_max <= 16):
    print("Según las temperaturas registradas, nos encontramos en invierno")
elif (temperatura_min >= 8 and temperatura_min <= 12) and (temperatura_max >= 22 and temperatura_max <= 26):
    print("Según las temperaturas registradas, nos encontramos en primavera")
else:
    print("No es posible determinar en qué epoca del año fueron registradas las temperaturas")

print("Ejercicio de profundización 4 resuelto")
