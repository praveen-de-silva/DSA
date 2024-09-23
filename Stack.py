# ====================
# Stack Data Structure
# ====================

class Stack:
    def __init__(self, size):
        self.buffer = [None]*size
        self.size = size
        self.length = 0

    def __str__(self):
        return f'{self.buffer}' # to show the queue

    def isEmpty(self):
        if self.length==0:
            return True
        return False

    def push(self, item):
        if self.length<self.size:
            self.buffer[self.length] = item
            self.length += 1
            return True
        print('Stack is already full!')
        return False

    def pop(self):
        if not self.isEmpty():
            pop_item = self.buffer[self.length-1]
            self.buffer[self.length-1] = None             
            self.length -= 1
            return pop_item
        print('Nothing to pop!')
        return None

    def getLength(self):
        return self.length

    def getHead(self):
        if not self.isEmpty():
            return self.buffer[self.length-1]
        return False

    def getTail(self):
        if not self.isEmpty():
            return self.buffer[0]
        return False
        
s1 = Stack(5)
print(f'Is Empty : {s1.isEmpty()}')

s1.pop()
s1.push(2)
s1.push(4)
s1.push(6)
s1.push(8)
s1.push(10)
s1.push(12)

print(f'length : {s1.getLength()}')
print(f'head : {s1.getHead()}')
