# You have a deck of shuffled cards ranging from 0 to 100,000,000. There are 2 sub-ordinate below you and two subordinates below them and it goes on.

# The job of the sub-ordinate is to split the deck of cards that they received and give it to two sub-ordinate of them. If they receive a deck of cards from their subordinates, they merge it in an ascending order and give it their higher level.

# If a subordinate received only two cards, then he/she himself/herself arrange in ascending order give it back to that to the superior.

# If a subordinate received only one card, then he/she will give back that to the superior.
# Your task is to find how many people (including you) are required to sort the cards and print the sorted deck of cards and number of people required as a tuple.

# Write the function def subordinates(L):
def merge(A, B):
    m, n = len(A), len(B)
    c, i, j, k = [], 0, 0, 0
    while k < m + n:
        if i == m:
            c.extend(B[j:])
            k = k + n - j
        elif j == n:
            c.extend(A[i:])
            k = k + m - i
        elif A[i] < B[j]:
            c.append(A[i])
            i, k = i + 1, k + 1
        else:
            c.append(B[j])
            j, k = j + 1, k + 1
    return c

def mergesort(L):
    global c
    c = c + 1
    n = len(L)
    if n == 2:
        return L if L[0] < L[1] else L[::-1]
    if n <= 1:
        return L
    m = n // 2
    l = mergesort(L[:m])
    r = mergesort(L[m:])
    L_ = merge(l, r)
    return L_

def subordinates(L):
    return mergesort(L), c
c = 0
