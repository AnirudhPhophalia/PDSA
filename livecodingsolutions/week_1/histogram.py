# Python function histogram(L) that takes as input a list of integers with repetitions and returns a list of pairs as follows:
    # For each number n that appears in L, there should be exactly one pair (n, r) in the list returned by the function, where r is the number of repetitions of n in L.
    # The final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.
def count(L):
    freq = {}
    for i in L:
        if i in freq.keys():
            freq[i] +=1
        else:
            freq[i] = 1
    return freq, freq.keys()
def histogram(L):
    freq, keys = count(L)
    nL = [(freq[i], i) for i in keys]
    nL.sort()
    finalL = [(t[1], t[0]) for t in nL]
    return finalL
L=eval(input())
print(histogram(L))