# Programa para ordenar una fila específica de una matriz bidimensional utilizando Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_matrix_row(matrix, row_index):
    # Verificar si el índice de fila es válido
    if row_index < 0 or row_index >= len(matrix):
        raise ValueError("Índice de fila inválido")

    # Crear una copia de la matriz para no modificar la original
    new_matrix = [row[:] for row in matrix]

    # Ordenar la fila especificada
    new_matrix[row_index] = bubble_sort(new_matrix[row_index])

    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Crear una matriz bidimensional 3x3
matrix = [
    [9, 2, 5],
    [1, 8, 3],
    [4, 6, 7]
]

# Fila a ordenar (por ejemplo, la fila 1, índice 0-based)
row_to_sort = 1

# Mostrar matriz original
print("Matriz original:")
print_matrix(matrix)

# Ordenar la fila especificada
sorted_matrix = sort_matrix_row(matrix, row_to_sort)

# Mostrar matriz con la fila ordenada
print(f"\nMatriz con la fila {row_to_sort + 1} ordenada:")
print_matrix(sorted_matrix)