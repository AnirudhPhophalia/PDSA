# A doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains three fields: two link fields (references to the previous and to the next node in the sequence of nodes) and one data field. So, it can be traversed in both directions.

# For the given class doubly_linked_list, create one method:

# insert_at_pos(data, pos): that accepts an integer data and inserts it into the list at the given pos position where 1 ≤ pos ≤ length(list).

# Note: Use the given linked list structure for implementation.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
      
    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:            
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    def insert_at_pos(self, data, pos):
        newnode = Node(data)
        if pos == 1:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            self.head = newnode
            if self.last is None:
                self.last = newnode
            return

        curr = self.head
        count = 1
        while curr and count < pos - 1:
            curr = curr.next
            count += 1

        if curr is None:  # Position is out of bounds
            return

        newnode.next = curr.next
        newnode.prev = curr
        if curr.next:
            curr.next.prev = newnode
        curr.next = newnode
        if newnode.next is None:
            self.last = newnode