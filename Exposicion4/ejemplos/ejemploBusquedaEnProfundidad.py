mapa = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 20},
    'C': {'A': 10, 'D': 5},
    'D': {'B': 20, 'C': 5, 'E': 15},
    'E': {'D': 15}
}

def buscar_ruta_profundidad(mapa, inicio, fin):
    visitados = set()
    pila = [(inicio, [inicio], 0)]
    
    while pila:
        (ciudad_actual, ruta, distancia) = pila.pop()
        
        if ciudad_actual == fin:
            return (ruta, distancia)
        
        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            
            for ciudad_vecina, distancia_vecina in mapa[ciudad_actual].items():
                if ciudad_vecina not in visitados:
                    pila.append((ciudad_vecina, ruta + [ciudad_vecina], distancia + distancia_vecina))
    
    return None

ruta, distancia = buscar_ruta_profundidad(mapa, 'A', 'E')
print("La ruta más corta es:", ruta)
print("La distancia total es:", distancia)

