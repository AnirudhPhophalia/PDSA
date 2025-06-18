# Consider a list L containing n integers, where each integer i is in the range [0, r) that is 0 <= i < r, r < 1000 and n >> r (n is much greater than r). Write a Python function sortInRange(L, r) to sort the list L in ascending order. Try to write a solution that runs in O(n + r) asymptotic complexity.

def sortInRange(L, r):
    countDict = dict.fromkeys(range(r), 0)
    for num in L:
        countDict[num] += 1
    index = 0
    for key in countDict.keys():
        for i in range(countDict[key]):
            L[index] = key
            index += 1