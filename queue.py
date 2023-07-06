class Queue2:
    """PRIMEIRO INSERIDO, PRIMEIRO REMOVIDO"""
    def __init__(self):
        self.last = None  # elemento que ta no topo
        self.first = None  # elemento que ta no inicio  (primeiro)
        self.size = 0

    def push(self, elem):
        """INSERE NA ULTIMA POSIÇÃO DA FILA"""
        new_node = Node(elem)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.size += 1

    def pop(self):
        """REMOVE O PRIMEIRO ELEMENTO DA FILA"""
        if self.first != None:
            elem = self.first.data
            self.first = self.first.next
            self.size -= 1
            print(f"Element removed: {elem}")
        else:
            raise IndexError("Fila está vazia")

    def peek(self):
        """PRINTA O PRIMEIRO ELEMENTO DA FILA"""
        if self.size > 0:
            print(f"Top is: {self.first.data}")
        else:
            raise IndexError("Stack is empty")

    def print(self):
        """PRINTA TODOS OS ELEMENTOS DA FILA"""
        if self.size > 1:
            node = self.first
            while node.next != None:
                print(f"{node.data}",end= " | ")
                node = node.next

            print(node.data) #printa o ultimo (que possui next == None)
        else:
            raise IndexError("Stack is empty")


# fila = Queue2()
# fila.push(3)
# fila.push(6)
# fila.push(87)
# fila.push(44)
# fila.push(432)
# fila.push(68)
# fila.push(77)
# fila.push(98)
# fila.peek()
# fila.print()
# fila.pop()
# fila.peek()
# fila.pop()
# fila.peek()
# fila.print()