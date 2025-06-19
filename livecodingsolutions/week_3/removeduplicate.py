# Consider an implementation of a linked list, where each node is created using the given class Node. Suppose it has a head variable that contains the reference to the first node of the linked list.

# You are given a non-empty linked list with n nodes, where these nodes are sorted in ascending order of their value. Your task is to remove nodes with duplicate values from the given list.

# Write a function removeDuplicate(head), where head is a reference to the first node of the sorted linked list, that removes nodes with duplicate values from the given linked list. The function should not return any value.

def removeDuplicate(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next