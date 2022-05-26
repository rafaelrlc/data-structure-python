import pandas
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # O NEXT REFERENCIA O PROXIMO OBJETO NODE (GUARDA)


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def append(self, elem):
        """INSERE NO FINAL"""
        new_node = Node(elem)
        if self.head == None: # primeira inserção
            self.head = new_node
            self.last = new_node
            self.size += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.size += 1

         # MENOS EFICIENTE
        # node = Node(elem)
        # if self.head != None:  #não for a primeira inserção
        #     pointer = self.head
        #     while pointer.next != None:
        #         pointer = pointer.next  # pointer.next é igual ao objeto que vem depois (next) , quando pointer.next for igual a none é pq esse é o ultimo elemento da lista e por isso não possui next
        #     pointer.next = node
        #     # esse pointer.next ->ERA<- igual a NULL, agora ele assegura o objeto do proximo elemento
        #
        # else: #se for a primeira inserção
        #     self.head = node
        #     self.last = node
        #     # dentro desse objeto o valor do elemento(data) e o que esta apontando(next)

    def printar(self):
        """PRINTA ELEMENTOS DA LISTA"""
        pointer = self.head
        print(pointer.data)  # printar head
        while pointer.next != None:
            print(pointer.next.data)
            pointer = pointer.next

    def index(self, elem):
        """RETORNA INDEX DO ELEMENTO NA LISTA"""
        counter = 0
        pointer = self.head
        while pointer != None:
            if pointer.data == elem:
                print(f"Index:{counter}")
                return counter

            pointer = pointer.next
            counter = counter + 1

        print(f"Element {elem} not found.")

    def insert(self, index, elem):
        """INSERE UM ELEMENTO EM UMA POSICAO QUALQUER NA LISTA"""

        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node

        else:
            pointer = self.head
            for i in range(index - 1):  # percorrer até o antecessor
                if pointer != None:
                    pointer = pointer.next
                else:
                    raise IndexError("list out of index")
            new_node = Node(elem)  # new element

            new_next = pointer.next
            pointer.next = new_node
            new_node.next = new_next



    def remove(self, elem):
        """REMOVER NÓ"""
        if self.head == None: #se lista ta vazia
            raise ValueError(f"{elem} is not in list")

        if self.head.data == elem:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            ancestor = self.head  #ancestor e pointer são ponteiros
            pointer = self.head.next
            while (pointer != None):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self.size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{elem} is not in list")


    def troca(self, elem):
        """TROCAR O ELEMENTO DO NÓ"""


    def insertAtFirst(self, elem):
        """INSERE NO COMEÇO"""
        new_first = Node(elem)
        new_first.next = self.head
        self.head = new_first
        self.size += 1








# lin = LinkedList()


# lin.append(3)
# lin.append(21)
# lin.append(34)
# lin.append(43)
# lin.append(66)
# lin.append(23)


# lin.printar()
# print("")
# lin.remove(66)

# lin.printar()

# lin.index(23)
# lin.insertAtFirst(33)
# lin.printar()





