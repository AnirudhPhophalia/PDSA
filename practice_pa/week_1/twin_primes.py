# return twin primes as a tuple

def prime(n):
    if n<2:
        return False
    for i in range(2,n//2 +1):
        if n%i == 0:
            return False
    return True

def Twin_Primes(n,m):
    r=[]
    for i in range(n,m-1):
        if prime(i) == True:
            if prime(i+2) == True:
                r.append((i,i+2))
    return r
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))