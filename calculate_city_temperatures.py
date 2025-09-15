import random

def calculate_city_temperatures(ciudades, dias_semana, num_semanas, temperaturas):
    """
    Calcula la temperatura promedio por ciudad y semana a partir de una matriz 3D de temperaturas.
    
    Parámetros:
    - ciudades: Lista de nombres de ciudades
    - dias_semana: Lista de nombres de los días de la semana
    - num_semanas: Número de semanas
    - temperaturas: Matriz 3D [ciudades][días][semanas] con datos de temperatura
    
    Retorna:
    - promedios: Diccionario con promedios por ciudad y semana
    """
    num_dias = len(dias_semana)
    promedios = {}
    
    for c, ciudad in enumerate(ciudades):
        promedios[ciudad] = []
        for s in range(num_semanas):
            suma_temperaturas = 0
            for d in range(num_dias):
                suma_temperaturas += temperaturas[c][d][s]
            promedio = suma_temperaturas / num_dias
            promedios[ciudad].append(promedio)
    
    return promedios

# Ejemplo de uso
if __name__ == "__main__":
    # Definir parámetros
    ciudades = ["Madrid", "Barcelona", "Sevilla"]
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    num_ciudades = len(ciudades)
    num_dias = len(dias_semana)
    num_semanas = 2
    
    # Generar matriz 3D de temperaturas aleatorias
    temperaturas = [[[random.uniform(0, 40) for _ in range(num_semanas)] for _ in range(num_dias)] for _ in range(num_ciudades)]
    
    # Mostrar matriz generada
    print("Matriz de temperaturas generada:")
    for c, ciudad in enumerate(ciudades):
        print(f"\nCiudad: {ciudad}")
        for d, dia in enumerate(dias_semana):
            print(f" {dia}: {temperaturas[c][d]}")
    
    # Calcular promedios
    promedios = calculate_city_temperatures(ciudades, dias_semana, num_semanas, temperaturas)
    
    # Mostrar resultados
    print("\nPromedios de temperaturas por ciudad y semana:")
    for ciudad, proms in promedios.items():
        for s, promedio in enumerate(proms):
            print(f"Ciudad: {ciudad}, Semana {s+1}: {promedio:.2f} °C")