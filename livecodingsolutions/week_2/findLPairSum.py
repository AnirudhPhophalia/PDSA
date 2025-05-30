# Write a Python function findPair(L, pairSum) that return True if there exist a pair of integers in L whose sum is equal to x, False otherwise. Try to write a solution which is O(nlogn) or better.

def findPair(L,X):
    L.sort()
    left=0
    right = len(L) -1
    while(left<right):
        sum = L[left] +L[right]
        if (sum == X):
            return True
        elif(sum>X):
            right-=1
        else:
            left+=1
    return False
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))