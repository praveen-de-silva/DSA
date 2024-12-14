import Queue_LinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

def postOrderTraversal(rootNode):
    if not rootNode:
        return None
    
    postOrderTraversalOrderTraversal(rootNode.rightChild)
    postOrderTraversalOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
            
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)

            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, value):
    if not rootNode:
        return 
    if rootNode.data == value:
        return True
    if rootNode.data > value and rootNode.leftChild:
        return searchNode(rootNode.leftChild, value)
    if rootNode.data < value and rootNode.rightChild:
        return searchNode(rootNode.rightChild, value)
    return False

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode

    disbalanceNode.height = max(disbalanceNode.leftChild.height, disbalanceNode.rightChild.height) + 1
    newRoot.height = max(newRoot.leftChild, newRoot.rightChild) + 1
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode

    disbalanceNode.height = max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild)) + 1
    newRoot.height = max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)) + 1
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif  nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)) + 1
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.data: # LL condition
        return rightRotate(rootNode)
    elif balance > 1 and nodeValue > rootNode.data: # LR condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    elif balance < -1 and nodeValue < rootNode.data: # RL condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)        
    elif balance < -1 and nodeValue > rootNode.data: # RR condition
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    # case 1 : rootNode is None
    if not rootNode:
        return rootNode

    # case 2 : rotation is not required
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # case 2.1 : 'node' to be deleted has a child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        else:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        # case 2.2 : 'node' to be deleted has 2 children
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    # case 3 : rotation is required
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "AVL has been successfully deleted!"




avl = AVLNode(5)
avl = insertNode(avl, 10)
avl = insertNode(avl, 15)
avl = insertNode(avl, 20)

levelOrderTraversal(avl)

# avl = deleteNode(avl, 20)
# levelOrderTraversal(avl)

