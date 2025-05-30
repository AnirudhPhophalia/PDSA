# Complete the Python function mergeInPlace(A, B) that accepts two MyLists A and B containing integers that are sorted in ascending order and merges them in place (without using any other list) such that after merging, A and B are still sorted in ascending order with the smallest element of both MyLists as the first element of A.
def mergeInPlace(A, B):
  m = len(A)
  n = len(B)
  if (m < 1 or n < 1):
    return 
  
  # Find the smaller list of A and B.
  for i in range(0, m):
    # A and B are already sorted. B[0] will always be least in B, 
    # as we will maintain its sortedness .
    if (A[i] > B[0]):
      A.swap(i, B, 0)
       
      # move `B[0]` to its correct position in B to maintain the sortedness of B
      j = 0
      while(j < n - 1 and B[j] > B[j + 1]):
        B.swap(j+1, B, j)        
        j += 1