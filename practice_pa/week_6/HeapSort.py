# Function heapSort(arr) sorts the array arr using max heap.
# Complete the function heapify(arr, n, i), that takes three arguments:
#     arr is the max heap array,
#     n is the number of elements in heap arr
#     i is the index of element that needs to be heapified
#     and heapifies the array from index 0 to n-1 with respect to element at index i.

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

L = [int(item) for item in input().split(" ")]
heapSort(L)
print(*L)