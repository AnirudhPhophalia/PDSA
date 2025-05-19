# Python function binarySearchIndexAndComparisons(L, k) that accepts a list L sorted in ascending order and an integer k and returns a tuple (True/False, numComparisons). The first part of this tuple will be True if k is present in L, False otherwise. The second part of the tuple is an integer which gives the number of elements in L that are actually compared to k while searching it in the list L using binary search.
def binarySearchIndexAndComparisons(L, k):
    s = len(L)
    if s == 0:
        return (False, 0)
    left = 0
    right = s - 1
    c = 0
    while left <= right:
        mid = (left + right) // 2
        c += 1
        if k == L[mid]:
            return (True, c)
        elif k < L[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return (False, c)
