# Write a Python function KminGreaterThan(arr, k, num), that accepts an unsorted list arr, two numbers k and num, returns True if the kth smallest element in the list arr is greater than or equal to num, otherwise returns False. Try to write a solution that runs in O(n log k) time.

import heapq

def KminGreaterThan(arr, k, num):
    if k > len(arr):
        return False

    # Use a max-heap of size k, so push negative values
    max_heap = []

    for val in arr:
        heapq.heappush(max_heap, -val)
        if len(max_heap) > k:
            heapq.heappop(max_heap)  # remove largest among k+1 elements

    # The top of the max-heap is the k-th smallest (negated back)
    kth_smallest = -max_heap[0]
    return kth_smallest >= num
