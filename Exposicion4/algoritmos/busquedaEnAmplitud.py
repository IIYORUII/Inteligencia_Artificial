from collections import deque

def bfs(grafo, inicio, objetivo):
    cola = deque([inicio])
    visitados = set()
    
    while cola:
        nodo = cola.popleft()
        if nodo == objetivo:
            ruta = []
            while nodo is not None:
                ruta.append(nodo)
                nodo = grafo[nodo][1]
            return ruta[::-1]
        
        visitados.add(nodo)
        for vecino in grafo[nodo][0]:
            if vecino not in visitados:
                grafo[vecino][1] = nodo
                cola.append(vecino)
                
    return None


