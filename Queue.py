# ====================
# Queue Data Structure
# ====================

class Queue:
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

    def enqueue(self, item):
        if self.length<self.size:
            self.buffer[self.length] = item
            self.length += 1
            return True
        print('Queue is already full!')
        return False

    def dequeue(self):
        if not self.isEmpty():
            pop_item = self.buffer[0]
            
            for i in range(self.length-1):
                self.buffer[i] = self.buffer[i+1]
                
            self.length -= 1
            return pop_item
        print('Nothing to remove!')
        return None

    def getLength(self):
        return self.length

    def getHead(self):
        if not self.isEmpty():
            return self.buffer[0]
        return False

    def getTail(self):
        if not self.isEmpty():
            return self.buffer[self.length-1]
        return False
        
q1 = Queue(5)
print(f'Is Empty : {q1.isEmpty()}')

q1.dequeue()
q1.enqueue(2)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(8)
q1.enqueue(10)
q1.enqueue(12)

print(f'length : {q1.getLength()}')
print(f'head : {q1.getHead()}')
