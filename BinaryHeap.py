class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(rootNode.heapSize):
            print(rootNode.customList[i+1])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = index // 2
    if index <= 1:
        return
    
    if heapType == 'min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    
    elif heapType == 'max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is already full!"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Successfully inserted!"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex: # no children in the current index
        return
    elif rootNode.heapSize == leftIndex: # only one children in the current index
        if heapType == 'min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else: # having both children
        if heapType == 'min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = rootNode.customList[leftIndex]
            else:
                swapChild = rootNode.customList[rightIndex]

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize==0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

def deleteBHT(rootNode):
    rootNode.customList = None

nbh = Heap(9)
insertNode(nbh, 54, 'max')
insertNode(nbh, 26, 'max')
insertNode(nbh, 93, 'max')
insertNode(nbh, 17, 'max')
insertNode(nbh, 77, 'max')
insertNode(nbh, 31, 'max')
insertNode(nbh, 64, 'max')
insertNode(nbh, 55, 'max')
insertNode(nbh, 20, 'max')

# extractNode(nbh, 'max')
# print(sizeofHeap(nbh))

# deleteBHT(nbh)

levelOrderTraversal(nbh)
