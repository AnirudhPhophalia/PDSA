# Write a Python function listUnion(L1, L2) that accepts two integer lists L1 and L2 and return a list that is the union (L1 ∪ L2) of the two lists and is sorted in ascending order. Try to write a solution that runs in O(n log n) time.

# L1 contains all distinct integers and L2 contains all distinct integers, but there can be many elements common between L1 and L2.

# List L1 ∪ L2 contains all distinct elements of L1 and L2 combined, and is sorted in ascending order.

def listUnion(L1, L2):
    return sorted(set(L1) | set(L2))

set1 = [int(item) for item in input().split()]
set2 = [int(item) for item in input().split()]
print(*listUnion(set1, set2))