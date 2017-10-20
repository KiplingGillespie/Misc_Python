import math
import random
import time

#Modular Exponentiation
def modexp(integer, exponant, N):
    if exponant == 0:
        return 1
    z = modexp(integer, math.floor(exponant/2), N)
    if (exponant%2) == 0:
        return (z*z)%N
    else:
        return (integer*z*z)%N
    
#Greatest Common Divisor using Euclidian Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

#Greatest Common Divisor using exteded Euclidian Algorithm
def egcd(a, b):
    if b == 0: 
        return (1, 0, a)
    xp, yp, d = egcd(b, a%b)
    return (yp, xp - (math.floor(a/b)*yp), d)

#Test Primality of p using Fermat's Little Theorem
def primality(p, accuracy = 10):
    
    if (not p&1):
        return False
    elif p == 2:
        return True
    
    for x in range(1, accuracy):
        a = random.randint(2, p-1)
        res = modexp(a, p-1, p)
        if res == 1:
            continue
        else:
            return False
    return True

#Generate a prime number that has 64 bits.
def genprime(bindigits = 64):
    largest = (2**bindigits)-1
    smallest = (2**(bindigits-1))
    
    a = random.randint(smallest, largest)
    isPrime = primality(a, 10)
    
    tries= 0
    while(not isPrime):
        tries+=1
        a = random.getrandbits(bindigits)
        isPrime = primality(a)
    
    print("Found prime after", tries, "tries.")
    return a 

# PiFunc calculates how many prime numbers there are less than x
def PiFunc(x):
    return x/math.log(x)

#ProbPrime is supposed to calculate the chance of randomly selecting a prime
# number from a range of integers. It doesn't really work yet.
def ProbPrime(binBits):
    largest = (2**binBits)-1
    smallest = (2**(binBits-1))
    myRange = smallest-1
    probability = (PiFunc(largest)-PiFunc(smallest))/myRange*100
    return probability
    

def main():
    random.seed()
    avgRunTime = 0; 
    numRuns = 10
    bits = 64
    
    print(ProbPrime(bits), "chance of finding prime")
    
    #now lets try and generate a large number.
    for i in range(0, numRuns):
        #start stop watch for this run
        startTime = time.time()
        
        #calculate a prime number and print it when found
        prime = genprime(bits)
        print(prime)
        
        #Stop watch for this run
        endTime = time.time();
        
        avgRunTime+=endTime-startTime
        
    avgRunTime /= numRuns
    print("Average Run Time Per Prime: ", avgRunTime)
    
main()
