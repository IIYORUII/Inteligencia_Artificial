from queue import PriorityQueue

def busqueda_A_estrella(grafo, inicio, objetivo, heuristica, coste):
    visitados = set()
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, inicio, [inicio]))
    
    while not cola_prioridad.empty():
        costo_actual, nodo_actual, ruta_actual = cola_prioridad.get()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            if nodo_actual == objetivo:
                return ruta_actual
            
            for vecino, costo_vecino in grafo[nodo_actual].items():
                if vecino not in visitados:
                    costo_total = costo_actual + costo_vecino + heuristica[vecino]
                    ruta_actualizada = ruta_actual + [vecino]
                    cola_prioridad.put((costo_total, vecino, ruta_actualizada))
    
    return None

