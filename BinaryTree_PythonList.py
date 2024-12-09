class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def __str__(self):
        return str(self.customList)

    def insertNode(self, value):
        if self.lastUsedIndex+1==self.maxSize:
            return 'BT is already full!'
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return 'Values have been successfully inserted!'

    def searchNode(self, target):
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == target:
                return i
        return False

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index * 2)
        print(self.customList[index])
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index * 2)
        print(self.customList[index])
        self.preOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(1, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'There is nothing to delete'
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'Success'
        else:
            return False

    def deleteBT(self):
        self.customList = None
        self.lastUsedIndex = None
        self.maxSize = None
        return 'Successfully deleted!'
        
        

newBT = BinaryTree(8)
newBT.insertNode('Dirnks')
newBT.insertNode('Hot')
newBT.insertNode('Cool')
newBT.insertNode('Tea')
newBT.insertNode('Coffee')
newBT.insertNode('Coca')
newBT.insertNode('Fanta')

print(newBT)

# print(newBT.searchNode('Fanta'))
# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal(1)
# newBT.postOrderTraversal(1)
# newBT.levelOrderTraversal(1)

newBT.deleteNode('Dirnks')
print(newBT)


print(newBT)