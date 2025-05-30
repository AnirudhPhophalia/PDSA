# returns true if an integer can be written as a product of two primes

def factors(n):
    factorlist = []
    for i in range(1, n+1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist

def isprime(n):
    return factors(n) == [1, n]

def prime_product(n):
    for i in range(1, n+1):
        if n % i == 0:
            if isprime(i) and isprime(n // i):
                return True
    return False
n = int(input())
print(prime_product(n))