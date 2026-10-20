"""
EJEMPLO: 
un profesor necesita crear un progrma que le ayude a calcular el promedio de notas de un salon de clase,
el ingresa el nombre y el valor de la nota final de cada estudiante,al final necesita saber cual es el mejor
estudiante y el promedio de todo el curso

cada nota es de: 0 a 5.0

"""

cantidad_est= int(input("catidad de estudiantes"))
mejor_est= ""
nota_mayor = 0.0
suma = 0.0
promedio = 0.0

for veces in range(1,cantidad_est+1):
        print("\nEstudiante #",veces)
        nombre =input("nombre")
        nota = float(input("nota"))

        suma = suma + nota #<- Acumuladores 

        if nota > nota_mayor: # Encuentrar el estudiante con mayor nota
            nota_mayor = nota
            mejor_est  = nombre

promedio = suma / cantidad_est

print("el promedoio del curso es:",promedio)
print("el  mejor estudiante es:",mejor_est,"con nota de :",nota_mayor) 