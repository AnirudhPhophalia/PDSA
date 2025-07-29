def median(A, B, sA, lA, sB, lB):
    n = lA - sA + 1
    # Base cases
    if n == 1:
        return (A[sA] + B[sB]) / 2
    if n == 2:
        return (max(A[sA], B[sB]) + min(A[lA], B[lB])) / 2
    
    m1 = sA + (n - 1) // 2
    m2 = sB + (n - 1) // 2

    if A[m1] == B[m2]:
        return A[m1]
    
    # if n is even, no need to add +1
    if A[m1] < B[m2]:
        return median(A, B, m1, lA, sB, sB + lA - m1)
    else:
        return median(A, B, sA, sA + lA - m1, m2, lB)

def findMedian(A, B):
    n = len(A)
    return median(A, B, 0, n-1, 0, n-1)
