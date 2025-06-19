# A doubly linked list is a linked data structure that consists of two header nodes that point to the first and last position in a sequence of linked records. Each node in the sequence contains three fields: One data field and two link fields (references to the previous and to the next node in the sequence of nodes) and. So, it can be traversed in both directions.

# For the given class doubly_linked_list, create two methods:

# insert_end(data): that accepts an integer data and inserts it into the list at the last position.

# delete_end(): Delete one element of the list from the last position.

# Note: Use given linked list structure to implementation. Write both operations (insert_end and delete_end) with O(1) time.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class doubly_linked_list:
  def __init__(self):
    self.head = None
    self.last = None
  def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # List is empty, head and last both point to new node
            self.head = self.last = new_node
        else:
            # Link the new node at the end and update last
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

  def delete_end(self):
        if self.last is None:
            # List is empty, nothing to delete
            return
        if self.head == self.last:
            # Only one node in the list
            self.head = self.last = None
        else:
            # Remove the last node and update last pointer
            self.last = self.last.prev
            self.last.next = None
            
