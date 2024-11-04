import math
import string
import numpy as np


#Principle of Sieve of eratosthenes
#https://code.activestate.com/recipes/117119/
def gen_primes(): # Generates an infinite sequence of prime numbers
  D = {}
  q = 2  # first integer to test for primality.

  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 

      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]
    q += 1

def fibArr():
    # Fibonacci sequence generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#hoiii - ich han mich i din code ghackt:)) vu mim ipad us - whäääckkkkkk:) liebi grüess - ilja


primes = gen_primes()
# primes = fibArr()
number_arr = []



while len(number_arr) < 26:
    mom = next(primes) % 26

    if(mom not in number_arr and mom != 0):
        number_arr.append(mom)
    else:
        while mom in number_arr or mom == 0:
            mom += 1
        number_arr.append(mom)

# number_arr.sort()
print(number_arr)