class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        if not isinstance(next_node, (Node, dict)) and next_node is not None:
            raise TypeError("next_node debe ser del tipo Node, dict o None")
        self.next_node = next_node


def cifrar_cesar(texto, desplazamiento):
    cabeza = None
    cola = None

    for char in texto:
        if char.isalpha():  # Solo ciframos letras
            desplazamiento_base = 65 if char.isupper() else 97
            # Aplicar el cifrado César
            nuevo_char = chr((ord(char) - desplazamiento_base + desplazamiento) % 26 + desplazamiento_base)
        else:
            nuevo_char = char  # No ciframos otros caracteres

        # Crear un nuevo nodo
        nuevo_nodo = Node(nuevo_char)
        
        # Añadir el nodo a la lista enlazada
        if cabeza is None:
            cabeza = nuevo_nodo
            cola = nuevo_nodo
        else:
            cola.set_next_node(nuevo_nodo)
            cola = nuevo_nodo

    return cabeza


def mostrar_lista_enlazada(cabeza):
    actual = cabeza
    resultado = ""
    while actual is not None:
        resultado += actual.get_value()
        actual = actual.get_next_node()
    return resultado


# Ejemplo de uso
texto_original = "Hola, Mundo!"
desplazamiento = 3
cabeza = cifrar_cesar(texto_original, desplazamiento)
texto_cifrado = mostrar_lista_enlazada(cabeza)
print("Texto Original:", texto_original)
print("Texto Cifrado:", texto_cifrado)