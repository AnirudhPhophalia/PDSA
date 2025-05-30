# Write a Python function sumsquare(L) that takes a nonempty list of integers as input and returns a list [odd, even], where odd is the sum of squares of all the odd numbers in L and even is the sum of squares of all the even numbers in L
def sumsquare(L):
    odd = 0
    even = 0
    for x in L:
        if x % 2 == 0:
            even += x**2
        else:
            odd += x**2
    return [odd, even]
L = eval(input())
print(sumsquare(L))