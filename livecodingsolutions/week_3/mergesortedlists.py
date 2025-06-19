# Consider an implementation of a linked list, where each node is created using the given class Node. Suppose it has a head variable that contains the reference to the first node of the linked list.

# You are given two non-empty linked lists with n and m nodes, where these nodes are sorted in ascending order of their value. Your task is to merge these two sorted linked lists into one sorted linked list.

# Write a function mergeSortedList(head1, head2), where head1 and head2 are references to the first nodes of two sorted linked lists. The function should return the reference of the first node of the merged sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Contains reference to the next node if it exists, otherwise None

def mergeSortedList(head1, head2):
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # Attach the remaining nodes
    if head1:
        tail.next = head1
    else:
        tail.next = head2

    return dummy.next
