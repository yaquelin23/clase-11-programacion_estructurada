#solicitar el numero de filas y columnas 
filas = int (input("Ingrese el numero de filas:"))
columnas = int(input("Ingresa el numero de columnas: "))

#Crear la matriz llena con la letra "A"
matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

#Mostrar la matriz resultante
print("\La matriz resultante es: ")
for fila in matriz:
    print(fila)