# Write a Python function findCommonElements(L1, L2) that accepts two integer lists L1 and L2 of same length n and return a list that contains elements that are common to both lists. Write a efficient solution that runs in O(nlogn) or better time.

# L1 contains all distinct integers and L2 contains all distinct integers, but there can be many elements common between L1 and L2.
# Returned list contains all elements that are common to L1 and L2. The elements in the returned list can be in any order.

def findCommonElements(L1, L2):
    L1_sorted = sorted(L1)
    L2_sorted = sorted(L2)
    result = []
    i = j = 0
    while i < len(L1_sorted) and j < len(L2_sorted):
        if L1_sorted[i] == L2_sorted[j]:
            result.append(L1_sorted[i])
            i += 1
            j += 1
        elif L1_sorted[i] < L2_sorted[j]:
            i += 1
        else:
            j += 1
    return result
