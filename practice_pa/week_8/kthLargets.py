# Write a Python function kthLargest(arr, k) that accepts a list arr of integers of size n and an integer k, such that k < = n and returns the kth largest integer in arr. The solution should run in O(n)O(n) time.

import random

def kthLargest(arr, k):
    def quickSelect(left, right, index_to_find):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if index_to_find == pivot_index:
            return arr[pivot_index]
        elif index_to_find < pivot_index:
            return quickSelect(left, pivot_index - 1, index_to_find)
        else:
            return quickSelect(pivot_index + 1, right, index_to_find)

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] > pivot_value:  # For kth largest, use >
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    n = len(arr)
    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and len(arr)")

    return quickSelect(0, n - 1, k - 1)

arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthLargest(arr, k))