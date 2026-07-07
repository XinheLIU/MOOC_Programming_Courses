# Classic Programming Question:
# find the n-th Monisen number. A number M is a Monisen number if M=2**P-1
# and both M and P are prime numbers. For example, if P=5, M=2**P-1=31, 5
# and 31 are both prime numbers, so 31 is a Monisen number.

import math

def isPrime(n):
  if n <= 1:
      return 0
  i = 2
  while i*i <= n:
      if n % i == 0:
          return 0
      i += 1
  return 1

def monisen(Nth):
    count = 0
    P = 1
    while count!= Nth:
        P += 1
        P_isPrime = isPrime(P)
        if(P_isPrime):
            M = int(math.pow(2,P) - 1)
            M_isPrime = isPrime(M)
            if(M_isPrime):
                if (count + 1 == Nth):
                    return(M)
                count += 1

print(monisen(int(input("What's the order of Monisen you want to find?"))))