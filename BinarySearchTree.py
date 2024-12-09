class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



def insertNode(rootNode, value):
    if rootNode == None:
        rootNode.data = value

    if value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insertNode(rootNode.leftChild, value)
    
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild, value)
    return 'Inserted successfully!'

def preOrderTraversal(rootNode):
    if not rootNode:
        return None
    
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return None
    
    inOrderTraversalOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    inOrderTraversalOrderTraversal(rootNode.leftChild)
            


bst = BSTNode(70)
bst.leftChild = BSTNode(50)
bst.rightChild = BSTNode(90)

bst.leftChild.leftChild = BSTNode(30)
bst.leftChild.rightChild = BSTNode(60)
bst.rightChild.leftChild = BSTNode(80)
bst.rightChild.rightChild = BSTNode(100)

bst.leftChild.leftChild.leftChild = BSTNode(20)
bst.leftChild.leftChild.rightChild = BSTNode(40)

insertNode(bst, 10)
insertNode(bst, 95)

# print(bst.rightChild.rightChild.data)
preOrderTraversal(bst)

