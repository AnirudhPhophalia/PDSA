# Consider a list L containing n integers, where each integer i is in the range [0, r) that is 0 ≤ i < r, r < 1000 and n ≫ r (n much greater than r). Write a Python function sortInRange(L, r) to sort the list L in ascending order. Try to write a solution that runs in O(n + r) asymptotic complexity.
def sortInRange(L, r):
    # Create a dictionary with r keys for each integer in range r, initialize every value to 0
    countDict = dict.fromkeys(range(r), 0)
    # Iterate over the array and count each integer in the list
    for num in L:
        countDict[num] += 1
    index = 0
    # For key in countDict.keys():
    for key in countDict.keys():
        for i in range(countDict[key]):
            L[index] = key
            index += 1