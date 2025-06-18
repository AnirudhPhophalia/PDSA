# You have given a list of distinct integers ranging from 1 to n in increasing order. There is one number missing in list L. Find the missing number in the list L.

# Note: The worst case running time of your program should be: O(log n)

# Implement the function missing_number(L) that takes list L and returns the missing number.

def missing_number(L):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1
