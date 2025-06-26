# Given a list of integers sorted in ascending order, find the number of occurrences for a given element in the list. The worst case running time of your program should be 

# Write a function countOccurrence(AList, size, key) which returns the frequency of key in AList. If the element is not present in the list, your function should return 0.

def countOccurrence(AList, size, key):
    def find_first(low, high):
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if AList[mid] == key:
                first = mid
                high = mid - 1
            elif AList[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def find_last(low, high):
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if AList[mid] == key:
                last = mid
                low = mid + 1
            elif AList[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return last
    
    first_idx = find_first(0, size-1)
    if first_idx == -1:
        return 0
    last_idx = find_last(0, size-1)
    return last_idx - first_idx + 1
