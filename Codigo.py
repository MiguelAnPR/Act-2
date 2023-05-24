# Definición de la base de conocimiento en reglas lógicas
base_conocimiento = {
    "conexiones": {
        "A": [("B", 5), ("C", 3)],
        "B": [("D", 2)],
        "C": [("D", 4), ("E", 6)],
        "D": [("F", 8)],
        "E": [("F", 3)],
        "F": []
    }
}

# Implementación del algoritmo de búsqueda A*
def buscar_ruta_A_estrella(origen, destino, base_conocimiento):
    # Definir función heurística (en este caso, distancia en línea recta)
    def heuristica(ciudad):
        coordenadas = {
            "A": (0, 0),
            "B": (1, 2),
            "C": (3, 1),
            "D": (2, 3),
            "E": (4, 4),
            "F": (5, 5)
        }
        x1, y1 = coordenadas[ciudad]
        x2, y2 = coordenadas[destino]
        return abs(x2 - x1) + abs(y2 - y1)

    # Inicializar lista de nodos abiertos y cerrados
    nodos_abiertos = [(origen, 0, heuristica(origen), [])]
    nodos_cerrados = []

    while nodos_abiertos:
        # Obtener el nodo actual (el de menor costo f)
        nodo_actual = min(nodos_abiertos, key=lambda x: x[1] + x[2])
        ciudad_actual, costo_g, _, ruta_actual = nodo_actual

        if ciudad_actual == destino:
            # Se ha llegado al destino, retornar la ruta encontrada
            return ruta_actual + [ciudad_actual]

        # Mover el nodo actual de la lista de abiertos a cerrados
        nodos_abiertos.remove(nodo_actual)
        nodos_cerrados.append(nodo_actual)

        # Obtener las conexiones de la ciudad actual desde la base de conocimiento
        conexiones = base_conocimiento["conexiones"].get(ciudad_actual, [])

        for ciudad, costo in conexiones:
            # Calcular el costo total para el siguiente nodo
            costo_total = costo_g + costo
            nodo_siguiente = (ciudad, costo_total, heuristica(ciudad), ruta_actual + [ciudad])

            if nodo_siguiente in nodos_cerrados:
                # El nodo siguiente ya fue explorado, pasar al siguiente
                continue

            if nodo_siguiente not in nodos_abiertos:
                # Agregar el nodo siguiente a la lista de abiertos
                nodos_abiertos.append(nodo_siguiente)
            else:
                # Actualizar el nodo existente si el nuevo costo es menor
                indice = nodos_abiertos.index(nodo_siguiente)
                if nodos_abiertos[indice][1] > nodo_siguiente[1]:
                    nodos_abiertos[indice] = nodo_siguiente

    # No se encontró una ruta desde el origen al destino
    return None
    # Utilizando el sistema inteligente para encontrar la mejor ruta

# Punto de partida y destino
origen = "A"
destino = "F"

# Llamada a la función de búsqueda A*
ruta_optima = buscar_ruta_A_estrella(origen, destino, base_conocimiento)

if ruta_optima:
    print("La mejor ruta desde {} hasta {} es: {}".format(origen, destino, "->".join(ruta_optima)))
else:
    print("No se encontró una ruta desde {} hasta {}".format(origen, destino))