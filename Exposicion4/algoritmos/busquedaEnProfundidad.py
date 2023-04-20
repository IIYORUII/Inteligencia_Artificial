def dfs(grafo, inicio, objetivo):
    visitados = set()
    ruta = []
    pila = [inicio]
    
    while pila:
        nodo_actual = pila.pop()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            ruta.append(nodo_actual)
            
            if nodo_actual == objetivo:
                return ruta
            
            for vecino in grafo[nodo_actual][0]:
                if vecino not in visitados:
                    pila.append(vecino)
                    
    return None

