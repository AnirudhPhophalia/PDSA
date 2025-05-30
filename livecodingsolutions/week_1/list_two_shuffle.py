# shuffle(L1, L2) that takes two lists, L1 and L2 as input, and returns a list consisting of the first element in L1, then the first element in L2, then the second element in L1, then the second element in L2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.
def shuffle(L1, L2):
    if len(L1) < len(L2):
        minlength = len(L1)
    else:
        minlength = len(L2)
    shuffled = []
    for i in range(minlength):
        shuffled.append(L1[i])
        shuffled.append(L2[i])
    shuffled = shuffled + L1[minlength:] + L2[minlength:]
    return(shuffled)
    
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))