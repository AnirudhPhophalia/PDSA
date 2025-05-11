# Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. It states that every even number greater than 2 is the sum of two prime numbers.
# Write a function Goldbach(n) where n is a positive even number (n > 2) that returns a list of tuples. In each tuple (a, b) where a <= b, a and b should be prime numbers and the sum of a and b should be equal to n.

# prime function hai yeh
def prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True
  

#  ek prime doosra number - x should be prime
def Goldbach(n):
  r=[]
  for i in range((n//2)+1):
    if prime(i)==True:
      if prime(n-i)==True:
        r.append((i,n-i))
  return(r)
  
  
n=int(input())
print(sorted(Goldbach(n)))