# Given a circularly sorted integer list, find the total number of times the list is rotated. Assume there are no duplicates in the list, and the rotation is in the anti-clockwise direction.

# For example:

# Sorted List L = [1,2,3,4,5]

# After one anti clock wise rotation: L = [5, 1, 2, 3, 4]

# After Second anti clock wise rotation: L = [4, 5, 1, 2, 3]

# Write a function findRotationCount(L) that accept a sorted list L with n elements which is circularly rotated k times where 0 <= k < n. the function returns the value of k. Write the solution code of complexity O(logn).

def findRotationCount(L):
    low, high = 0, len(L) - 1
    n = len(L)
    
    while low <= high:
        # If the subarray is already sorted, the lowest element is at low
        if L[low] <= L[high]:
            return low
        
        mid = (low + high) // 2
        next_index = (mid + 1) % n
        prev_index = (mid - 1 + n) % n
        
        # Check if mid is the minimum (pivot)
        if L[mid] <= L[next_index] and L[mid] <= L[prev_index]:
            return mid
        
        # Decide which half to go: pivot lies in unsorted half
        if L[mid] <= L[high]:
            # Right half is sorted, pivot in left half
            high = mid - 1
        else:
            # Left half is sorted, pivot in right half
            low = mid + 1
    
    return 0  # if no rotation
    