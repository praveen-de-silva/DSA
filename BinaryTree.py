class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'(Val : {self.data}, L : {self.left}, R : {self.right})'


class BinaryTree:
    def __init__(self, head_val):
        self.head = None
        self.tail = None
        self.length = 0

def preOrderTraversal(root_node):
    if root_node:
        print(root_node.value)
        preOrderTraversal(root_node.left)
        preOrderTraversal(root_node.right)
    return

def postOrderTraversal(root_node):
    if root_node:
        postOrderTraversal(root_node.left)
        postOrderTraversal(root_node.right)
        print(root_node.value)
    return

def inOrderTraversal(root_node):
    if root_node:
        inOrderTraversal(root_node.left)
        print(root_node.value)
        inOrderTraversal(root_node.right)
    return
        

tree = Node('Drinks')

cold = Node('1. Cold')
hot = Node('2. Hot')
cola = Node('1.1. Cola')
fanta = Node('1.2. Fanta')
tea = Node('2.1. Tea')
coffee = Node('2.2. Coffee')

tree.left = cold
tree.right = hot
cold.left = cola
cold.right = fanta
hot.left = tea
hot.right = coffee


##postOrderTraversal(tree)
inOrderTraversal(tree)
