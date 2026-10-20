"""
Sintaxis de la funcion range()

range([inicio],fin,[paso])  # El inicio y el paso son obciones, fin es obligatorio

-El inicio es 0 por defecto, si no se indica
-El paso es 1 por defecto, si no se indica

-la funcio range genera una serie de numeros enteros entre el inicio y el fin -1
, con un  incremento dado por el paso
"""
#caso 1 : range(fin)

print(list(range(10))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(101))) # 0, 1, 2,...,100
print(list(range(32)))  # 0,1 , 2, ...,31

#caso 2 : range(incio,fin)

print(list(range(3,10))) # 3, 4, 5,....,9
print(list(range(11,13))) # 11, 12
print(list(range(1001,1002))) # 1001 

#caso 3 : range(inicio,fin,paso)

print(list(range(3,20,2))) # 3, 5, 7, 9, 11, 13, 15, 17, 19
print(list(range(3,21,2))) # 3, 5,7,....,17,19 porque va de dos en dos y como es fin -1 el 21 no va
print(list(range(5,51,5))) # los 10 primeros multiplos de 5 
print(list(range(16,25,2)))# los 5 primeros pares del 15
print(list(range(21,0,-2))) # imprimir los impares desdes el 21 al 1


