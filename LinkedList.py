class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return f'[{self.value}] --> {self.next.value}'
        else:
            return f'[{self.value}] --> {None}'

class LinkedList:
    def __init__(self, value=None):
        if value!=None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def __str__(self):
        crnt_node = self.head
        rslt_list = []

        while crnt_node:
            rslt_list.append(str(crnt_node.value))
            crnt_node = crnt_node.next

        rslt = ' --> '.join(rslt_list)
        return rslt
            
L = LinkedList(10)
L.head.next = Node(20)
L.head.next.next = Node(30)
print(L)