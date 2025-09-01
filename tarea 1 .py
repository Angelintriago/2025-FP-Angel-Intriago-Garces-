# Crear una matriz bidimensional de 3x3
matrix = [
    [4, 7, 2],
    [9, 3, 5],
    [1, 8, 6]
]

# Función para buscar un valor en la matriz
def search_matrix(matrix, target):
    # Recorrer cada fila y columna de la matriz
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True, i, j  # Retorna True y la posición (fila, columna)
    return False, -1, -1  # Retorna False si no se encuentra

# Valor a buscar
target_value = 8

# Llamar a la función de búsqueda
found, row, col = search_matrix(matrix, target_value)

# Mostrar resultado
if found:
    print(f"El valor {target_value} se encontró en la posición ({row}, {col})")
else:
    print(f"El valor {target_value} no se encontró en la matriz")