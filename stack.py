class Stack:
    #next = elemento anterior
    def __init__(self):
        self.top = None # elemento que ta no topo
        self.size = 0

    def push(self, elem):
        """INSERE NO TOPO"""
        node = Node(elem)
        node.next = self.top # interliga ao antigo topo
        self.top = node # novo elemento VIRA o topo
        self.size += 1

    def pop(self):
        """REMOVE O TOPO"""
        if self.size > 0:
            node_pop = self.top # segura o valor do topo que será removido
            self.top = self.top.next
            self.size -= 1
            print(f"Removed:{node_pop}")
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        """PRINTA O TOPO"""
        if self.size > 0:
            print(f"Top is: {self.top.data}")
        else:
            raise IndexError("Stack is empty")

    def print(self):
        """PRINTA TODOS OS ELEMENTOS DA PILHA"""
        if self.size > 1:
            node = self.top
            while node.next != None:
                print(node.data)
                node = node.next

            print(node.data) #printa o ultimo (que possui next == None)
        else:
            raise IndexError("Stack is empty")