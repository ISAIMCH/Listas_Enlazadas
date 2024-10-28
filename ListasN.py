class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)
    

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.tamaño == 0:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.tamaño += 1
        return nuevo_nodo
    
    def eliminar(self, valor):
        if self.tamaño == 0:
            return False
        else:
            actual = self.primero
            if actual.valor == valor:  # Eliminar el primer nodo
                self.primero = actual.siguiente
                self.tamaño -= 1
                return actual
            
            while actual.siguiente is not None:
                if actual.siguiente.valor == valor:
                    nodo_a_eliminar = actual.siguiente
                    actual.siguiente = nodo_a_eliminar.siguiente
                    self.tamaño -= 1
                    return nodo_a_eliminar
                actual = actual.siguiente
            
            return False
    
    def __len__(self):
        return self.tamaño
    
    def __str__(self):
        resultado = "["
        actual = self.primero
        while actual is not None:
            resultado += str(actual)
            if actual.siguiente is not None:
                resultado += ", "
            actual = actual.siguiente
        resultado += "]"
        return resultado



# Ejemplo de uso
mi_lista = ListaEnlazada()

mi_lista.agregar(1)
mi_lista.agregar(2)
mi_lista.agregar(3)
mi_lista.agregar(4)

print(mi_lista)