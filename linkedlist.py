class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class MyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamano += 1
    
    def eliminar(self, valor):
        if not self.cabeza:
            return False
        
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            self.tamano -= 1
            return True
        
        return False
    
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print(" -> ".join(elementos))
    
    def obtener_tamano(self):
        return self.tamano


if __name__ == "__main__":
    lista = MyLinkedList()
    while True:
        print("\nOpciones:")
        print("1. Agregar un elemento")
        print("2. Eliminar un elemento")
        print("3. Buscar un elemento")
        print("4. Mostrar la lista")
        print("5. Mostrar tamaño de la lista")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            valor = input("Ingrese el valor a agregar: ")
            lista.agregar(valor)
        elif opcion == "2":
            valor = input("Ingrese el valor a eliminar: ")
            if lista.eliminar(valor):
                print("Elemento eliminado.")
            else:
                print("Elemento no encontrado.")
        elif opcion == "3":
            valor = input("Ingrese el valor a buscar: ")
            if lista.buscar(valor):
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")
        elif opcion == "4":
            print("Lista actual:")
            lista.mostrar()
        elif opcion == "5":
            print("Tamaño de la lista:", lista.obtener_tamano())
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
