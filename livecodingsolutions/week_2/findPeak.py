# Write a function Findpeak(L) that accepts a list L of n distinct elements and returns the peak element of the list. A list element is a peak if it is greater than its neighbors. For corner elements, we need to consider only one neighbor. Write a solution of O(logn) complexity. Consider that there is only one peak is in the list, L

def findPeakUtil(arr, low, high, n):
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] < arr[mid]) and (mid == n - 1 or arr[mid + 1] < arr[mid])):
        return arr[mid]

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    else:
        return findPeakUtil(arr, (mid + 1), high, n)

def Findpeak(L):
    n = len(L)
    return findPeakUtil(L, 0, n - 1, n)
