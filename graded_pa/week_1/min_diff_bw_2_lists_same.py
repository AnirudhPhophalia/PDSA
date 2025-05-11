# Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.
# Note - The list can contain more than one subset of p elements that have the same minimum difference value.

def find_Min_Difference(L,P):
    L.sort()
    N=P
    M=len(L)
    mi_d = max(L) - min(L)
    for i in range(M-N+1):
        if L[i+N-1] - L[i] < mi_d:
            mi_d = L[i+N-1] - L[i]
    return mi_d
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))