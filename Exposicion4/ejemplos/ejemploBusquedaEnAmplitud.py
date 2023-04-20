grafo_metro = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['C']
}

from collections import deque

def buscar_camino_bfs(grafo, inicio, objetivo):
    # Inicializar cola con la estación de inicio
    cola = deque([inicio])
    # Inicializar conjunto de estaciones visitadas
    visitado = set([inicio])
    # Inicializar diccionario de padres para construir el camino final
    padres = {inicio: None}
    
    # Mientras la cola no esté vacía
    while cola:
        # Sacar la primera estación de la cola
        estacion_actual = cola.popleft()
        
        # Si es la estación objetivo, construir y devolver el camino final
        if estacion_actual == objetivo:
            camino = [objetivo]
            padre = padres[objetivo]
            while padre:
                camino.append(padre)
                padre = padres[padre]
            camino.reverse()
            return camino
        
        # Si no es la estación objetivo, expandir la estación actual
        for estacion in grafo[estacion_actual]:
            if estacion not in visitado:
                visitado.add(estacion)
                cola.append(estacion)
                padres[estacion] = estacion_actual
    
    # Si no se encontró camino, devolver None
    return None

camino = buscar_camino_bfs(grafo_metro, 'A', 'F')
print(camino)  # ['A', 'C', 'F']

