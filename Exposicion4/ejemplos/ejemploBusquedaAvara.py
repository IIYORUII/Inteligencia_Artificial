import math

# Definición de las ciudades
cities = {
    'A': (0, 0),
    'B': (0, 3),
    'C': (4, 3),
    'D': (4, 0),
    'E': (2, 1),
    'F': (2, 2),
    'G': (3, 1),
    'H': (1, 1)
}

# Definición de la función heurística: distancia euclidiana
def heuristic(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Definición del problema: encontrar la ruta más corta para visitar las ciudades en orden
start_city = 'A'
end_city = 'H'
order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Implementación de la búsqueda ávida
current_city = start_city
visited_cities = [start_city]
while current_city != end_city:
    unvisited_cities = [c for c in order if c not in visited_cities]
    distances = {c: heuristic(current_city, c) for c in unvisited_cities}
    closest_city = min(distances, key=distances.get)
    visited_cities.append(closest_city)
    current_city = closest_city

# Impresión de la ruta más corta
print('Ruta más corta:', visited_cities)