def minheap(A):
    for i in range((len(A) - 2) // 2 + 1):
        if A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
            return False
    return True

def maxheap(A):
    for i in range((len(A) - 2) // 2 + 1):
        if A[i] < A[2*i + 1] or (2*i + 2 != len(A) and A[i] < A[2*i + 2]):
            return False
    return True

def Type_of_heap(A):
    if minheap(A) == True:
        return 'Min'
    if maxheap(A) == True:
        return 'Max'
    return 'None'

A=eval(input())
print(Type_of_heap(A))