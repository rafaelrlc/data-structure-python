import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def postorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left != None:
            self.postorder_traversal(node.left)
        if node.right != None:
            self.postorder_traversal(node.right)
        print(node.data, end=" ")

    def treeSum(self, root):
        if root is None:
            return 0
        else:
            leftSum = self.treeSum(root.left)
            rightSum = self.treeSum(root.right)
            return root.data + leftSum + rightSum  # quando o node a esquerda e direita foram verificados ele retorna o valor deles com o valor do node

    def armazenar_elementos2(self, lista, node=None): #METODO QUE USEI NA PROVA
        if node == None:
            return
        if node.left != None:
            self.armazenar_elementos2(lista, node.left)
        if node.right != None:
            self.armazenar_elementos2(lista, node.right)
        lista.append(node.data)
        return lista

    def armazenar_elementos(self, lista , node=None): #METODO MELHORADO
        if node == None:
            return None
        self.armazenar_elementos(lista, node.left)
        self.armazenar_elementos(lista, node.right)  
        lista.append(node.data)
        return lista
        

    def height_1(self, root):
        if root is None:
            return 0
        else:
            hleft = self.height_1(root.left)
            hright = self.height_1(root.right)
            return 1 + (max(hleft, hright))

    def mergeTrees(self, root1, root2):
        pass


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right

        #caso a arvore esteja vazia
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self):
        pass

    def remove(self):
        pass


lista = []
arvore1 = BinarySearchTree() #criou o nó
arvore1.insert(10)
arvore1.insert(5)
arvore1.insert(19)
arvore1.insert(1)
arvore1.insert(6)
arvore1.insert(7)
arvore1.insert(17)
arvore1.insert(21)


print(arvore1.armazenar_elementos2(lista, arvore1.root))
