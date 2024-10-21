# Se importa la clase Node desde el archivo Node_sandbox
from Node_sandbox import Node

# Definición de la clase LinkedList
class LinkedList:
    def __init__(self, value=None):
        """
        Constructor de la clase LinkedList.
        
        :param value: Valor opcional para inicializar el nodo cabeza.
        """
        self.head_node = Node(value)

    def get_head_node(self):
        """
        Devuelve el nodo cabeza de la lista.
        
        :return: Nodo cabeza de la lista.
        """
        return self.head_node
    
    def insert_beginning(self, new_value):
        """
        Inserta un nuevo nodo al principio de la lista.
        
        :param new_value: Valor que se asignará al nuevo nodo.
        """
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value):
        """
        Inserta un nuevo nodo al final de la lista.
        
        :param new_value: Valor que se asignará al nuevo nodo.
        """
        new_node = Node(new_value)
        if self.head_node is None:
            self.head_node = new_node
            return
        
        current_node = self.head_node
        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def stringify_list(self):
        """
        Convierte la lista en una cadena de texto.
        
        Cada valor de nodo se representa en una nueva línea.
        
        :return: Cadena que representa todos los valores de los nodos.
        """
        string_list = ""
        current_node = self.head_node
        
        while current_node is not None:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        
        return string_list

    def remove_node(self, value_to_remove):
        """
        Elimina un nodo con un valor específico de la lista.
        
        :param value_to_remove: Valor del nodo que deseas eliminar.
        """
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

    def swap_nodes(self, val1, val2):
        """
        Intercambia dos nodos en la lista basándose en sus valores.
        
        :param val1: Valor del primer nodo a intercambiar.
        :param val2: Valor del segundo nodo a intercambiar.
        """
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

        pivot = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(pivot)

    def find_penultimate_node(self):
        """
        Encuentra el antepenúltimo nodo de la lista enlazada.
        
        :return: El valor del antepenúltimo nodo o None si no existe.
        """
        current_node = self.head_node
        
        if current_node is None or current_node.get_next_node() is None:
            return None

        first_pointer = current_node
        second_pointer = current_node.get_next_node()

        while second_pointer.get_next_node() is not None:
            first_pointer = first_pointer.get_next_node()
            second_pointer = second_pointer.get_next_node()

        return first_pointer.get_value()

    def count_nodes(self):
        """
        Cuenta el número de nodos en la lista.
        
        :return: Número total de nodos en la lista.
        """
        count = 0
        current_node = self.head_node
        while current_node is not None:
            count += 1
            current_node = current_node.get_next_node()
        return count

    def search_node(self, value):
        """
        Busca un nodo con un valor específico en la lista.
        
        :param value: Valor a buscar.
        :return: True si el nodo existe, False en caso contrario.
        """
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next_node()
        return False

    def reverse_list(self):
        """
        Revierte la lista enlazada.
        """
        previous_node = None
        current_node = self.head_node
        while current_node is not None:
            next_node = current_node.get_next_node()  # Guarda el siguiente nodo.
            current_node.set_next_node(previous_node)  # Invierte el enlace.
            previous_node = current_node  # Mueve el puntero anterior.
            current_node = next_node  # Avanza al siguiente nodo.
        self.head_node = previous_node  # Actualiza la cabeza.

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una lista enlazada
    linked_list = LinkedList(10)  # Nodo cabeza con valor 10
    
    # Insertar nodos al principio
    linked_list.insert_beginning(20)
    linked_list.insert_beginning(30)
    linked_list.insert_beginning(40)
    
    # Insertar nodos al final
    linked_list.insert_end(50)
    linked_list.insert_end(60)
    
    # Imprimir la lista
    print("Lista después de inserciones:")
    print(linked_list.stringify_list())
    
    # Contar nodos
    print(f"Número total de nodos: {linked_list.count_nodes()}")
    
    # Buscar un nodo
    value_to_search = 30
    found = linked_list.search_node(value_to_search)
    print(f"¿El valor {value_to_search} está en la lista? {'Sí' if found else 'No'}")
    
    # Eliminar un nodo
    linked_list.remove_node(20)
    print("Lista después de eliminar el nodo con valor 20:")
    print(linked_list.stringify_list())
    
    # Intercambiar nodos
    linked_list.swap_nodes(30, 10)
    print("Lista después de intercambiar los nodos con valores 30 y 10:")
    print(linked_list.stringify_list())
    
    # Encontrar el antepenúltimo nodo
    antepenultimate_value = linked_list.find_penultimate_node()
    if antepenultimate_value is not None:
        print(f"El antepenúltimo nodo tiene el valor: {antepenultimate_value}")
    else:
        print("No hay antepenúltimo nodo en la lista.")
    
    # Revertir la lista
    linked_list.reverse_list()
    print("Lista después de revertir:")
    print(linked_list.stringify_list())