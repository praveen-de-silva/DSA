import Queue_LinkedList as queue

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

def minValueNode(bstNode):
    crntNode = bstNode
    while not crntNode.leftChild:
        crntNode = crntNode.leftChild
    return crntNode

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BST was successfully deleted!"

bst = BSTNode(70)
bst.leftChild = BSTNode(50)
bst.rightChild = BSTNode(90)

bst.leftChild.leftChild = BSTNode(30)
bst.leftChild.rightChild = BSTNode(60)
bst.rightChild.leftChild = BSTNode(80)
bst.rightChild.rightChild = BSTNode(100)

bst.leftChild.leftChild.leftChild = BSTNode(20)
bst.leftChild.leftChild.rightChild = BSTNode(40)

# insertNode(bst, 10)
# insertNode(bst, 95)

# print(bst.rightChild.rightChild.data)
# levelOrderTraversal(bst)
# print(searchNode(bst, 60))

# deleteNode(bst, 100)

levelOrderTraversal(bst)
