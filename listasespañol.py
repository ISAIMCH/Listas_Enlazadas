from Node_sandbox import Nodo

class ListaEnlazada:
    def __init__(self, valor=None):
        self.nodo_cabeza = Nodo(valor)

    def obtener_nodo_cabeza(self):
        return self.nodo_cabeza
    
    # Agregar un nuevo nodo al inicio de la lista
    def insertar_al_comienzo(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)
        nuevo_nodo.set_next_node(self.nodo_cabeza)
        self.nodo_cabeza = nuevo_nodo

    # Agregar un nuevo nodo al final de la lista
    def insertar_al_final(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)
        if self.nodo_cabeza is None:
            self.nodo_cabeza = nuevo_nodo
            return
        
        nodo_actual = self.nodo_cabeza
        while nodo_actual.get_next_node() is not None:
            nodo_actual = nodo_actual.get_next_node()
        nodo_actual.set_next_node(nuevo_nodo)

    # Convierte la lista en una cadena de texto
    def convertir_a_cadena(self):
        cadena_lista = ""
        nodo_actual = self.nodo_cabeza
        while nodo_actual is not None:
            cadena_lista += str(nodo_actual.get_value()) + " -> "
            nodo_actual = nodo_actual.get_next_node()
        return cadena_lista.rstrip(" -> ")  # Elimina el último " -> "
    
    # Elimina un nodo de la lista
    def eliminar_nodo(self, valor_a_eliminar):
        nodo_actual = self.nodo_cabeza

        if nodo_actual is None:
            return

        if nodo_actual.get_value() == valor_a_eliminar:
            self.nodo_cabeza = nodo_actual.get_next_node()
            return

        while nodo_actual is not None:
            nodo_siguiente = nodo_actual.get_next_node()
            if nodo_siguiente is not None and nodo_siguiente.get_value() == valor_a_eliminar:
                nodo_actual.set_next_node(nodo_siguiente.get_next_node())
                return
            nodo_actual = nodo_siguiente

    # Intercambia los valores de dos nodos
    def intercambiar_nodos(self, val1, val2):
        if val1 == val2:
            print("Los elementos son iguales, por lo que no es necesario intercambiarlos.")
            return

        nodo_actual = self.nodo_cabeza
        nodo1 = None
        nodo1_anterior = None
        nodo2 = None
        nodo2_anterior = None

        while nodo_actual is not None:
            if nodo_actual.get_value() == val1:
                nodo1 = nodo_actual
                break
            nodo1_anterior = nodo_actual
            nodo_actual = nodo_actual.get_next_node()

        nodo_actual = self.nodo_cabeza

        while nodo_actual is not None:
            if nodo_actual.get_value() == val2:
                nodo2 = nodo_actual
                break
            nodo2_anterior = nodo_actual
            nodo_actual = nodo_actual.get_next_node()

        if nodo1 is None or nodo2 is None:
            print("No es posible realizar el intercambio: uno o más elementos no están en la lista.")
            return

        if nodo1_anterior is None:
            self.nodo_cabeza = nodo2
        else:
            nodo1_anterior.set_next_node(nodo2)

        if nodo2_anterior is None:
            self.nodo_cabeza = nodo1
        else:
            nodo2_anterior.set_next_node(nodo1)

        # Intercambiar los nodos
        pivote = nodo1.get_next_node()
        nodo1.set_next_node(nodo2.get_next_node())
        nodo2.set_next_node(pivote)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una lista enlazada
    lista_enlazada = ListaEnlazada(1)  # Nodo cabeza con valor 1

    # Insertar nodos al principio
    lista_enlazada.insertar_al_comienzo(2)
    lista_enlazada.insertar_al_comienzo(3)
    lista_enlazada.insertar_al_comienzo(4)
    lista_enlazada.insertar_al_final(0)
    lista_enlazada.intercambiar_nodos(3, 4)
    lista_enlazada.eliminar_nodo(0)

    # Imprimir la lista
    print("Lista:")
    print(lista_enlazada.convertir_a_cadena())