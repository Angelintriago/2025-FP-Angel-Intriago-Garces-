import random

# Definir parámetros
ciudades = ["Madrid", "Barcelona", "Sevilla"]  # Lista de ciudades
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]  # Días de la semana
num_ciudades = len(ciudades)
num_dias = len(dias_semana)
num_semanas = 2  # Número de semanas (puedes ajustar este valor)

# Crear matriz 3D: [ciudades][días][semanas]
# Generar temperaturas aleatorias entre 0 y 40 °C como ejemplo
temperaturas = [[[random.uniform(0, 40) for _ in range(num_semanas)] for _ in range(num_dias)] for _ in range(num_ciudades)]

# Mostrar la matriz generada (opcional, para verificar los datos)
print("Matriz de temperaturas generada:")
for c, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for d, dia in enumerate(dias_semana):
        print(f"  {dia}: {temperaturas[c][d]}")

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
print("\nPromedios de temperaturas por ciudad y semana:")
for c, ciudad in enumerate(ciudades):
    for s in range(num_semanas):
        suma_temperaturas = 0
        for d in range(num_dias):
            suma_temperaturas += temperaturas[c][d][s]
        promedio = suma_temperaturas / num_dias
        print(f"Ciudad: {ciudad}, Semana {s+1}: {promedio:.2f} °C") 