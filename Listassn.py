from Node_sandbox import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    # Agregar un nuevo nodo al inicio de la lista
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # Agregar un nuevo nodo al final de la lista
    def insert_end(self, new_value):
        new_node = Node(new_value)
        if self.head_node is None:
            self.head_node = new_node
            return
        
        current_node = self.head_node
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    # Convierte la lista en una cadena de texto
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node is not None:
            string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()
        return string_list.rstrip(" -> ")  # Elimina el último " -> "
    
    # Elimina un nodo de la lista
    def remove_node(self, value_to_remove):
        current_node = self.head_node

        if current_node is None:
            return

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return

        while current_node is not None:
            next_node = current_node.get_next_node()
            if next_node is not None and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = next_node

    # Intercambia los valores de dos nodos
    def swap_nodes(self, val1, val2):
        if val1 == val2:
            print("Los elementos son iguales, por lo que no es necesario intercambiarlos.")
            return

        current_node = self.head_node
        node1 = None
        node1_prev = None
        node2 = None
        node2_prev = None

        while current_node is not None:
            if current_node.get_value() == val1:
                node1 = current_node
                break
            node1_prev = current_node
            current_node = current_node.get_next_node()

        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == val2:
                node2 = current_node
                break
            node2_prev = current_node
            current_node = current_node.get_next_node()

        if node1 is None or node2 is None:
            print("No es posible realizar el intercambio: uno o más elementos no están en la lista.")
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # Intercambiar los nodos
        pivot = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(pivot)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una lista enlazada
    linked_list = LinkedList(1)  # Nodo cabeza con valor 10

    # Insertar nodos al principio
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(3)
    linked_list.insert_beginning(4)
    linked_list.insert_end(0)
    linked_list.swap_nodes(3, 4)
    linked_list.remove_node(0)

    # Imprimir la lista
    print("Lista:")
    print(linked_list.stringify_list())
