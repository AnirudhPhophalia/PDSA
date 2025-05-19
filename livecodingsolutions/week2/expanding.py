# Write a function expanding(L) that takes a list of integers L as input and returns True if the absolute difference between each adjacent pair of elements strictly increases.
def expanding(L):
    diffs = []
    for i in range(len(L) - 1):
        diffs.append(abs(L[i+1] - L[i]))
    for i in range(len(diffs) - 1):
        if diffs[i+1] <= diffs[i]:
            return False
    return True
    
L = eval(input())
print(expanding(L))