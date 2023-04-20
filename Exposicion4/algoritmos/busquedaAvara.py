from queue import PriorityQueue

def busqueda_avida(grafo, inicio, objetivo, heuristica):
    visitados = set()
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((heuristica[inicio], inicio))
    ruta = []
    
    while not cola_prioridad.empty():
        nodo_actual = cola_prioridad.get()[1]
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            ruta.append(nodo_actual)
            
            if nodo_actual == objetivo:
                return ruta
            
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    prioridad = heuristica[vecino]
                    cola_prioridad.put((prioridad, vecino))
                    
    return None

