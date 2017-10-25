import math
import random
import time
import os

'''
Kipling Gillespie
August 2017
Last Updated: 10/25/2017


I wrote this program to teach myself python and practice
algorithms we were covering in my CS315 class at 
the University of Kentucky. 

'''

# Calculates the modular exponentiation of (integer^exponant) Mod N
# I need to write a non-recursive version of this method. When we try
# and calculate a 128 byte prime the program crashes due to 
# the stack overflowing from recursion. 
def modexp(integer, exponant, N):
    
    if exponant == 0:
        return 1
    
    z = modexp(integer, exponant//2, N)
    
    if (exponant%2) == 0:
        return (z*z)%N
    else:
        return (integer*z*z)%N

# Calculates the Greatest Common Divisor using Euclid's Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# Calculates the Greatest Common Divisor, and x and y using
# Euclid's Extended Algorithm
def egcd(a, b):
    if b == 0: 
        return (1, 0, a)
    xp, yp, d = egcd(b, a%b)
    return (yp, xp - (math.floor(a/b)*yp), d)


# Calculates whether p is prime or not b using Fermat's Little Theorem.
# the Accuracy variable tells the program how many random values for
# a the program should run
def primality(p, accuracy = 100):
    
    # we know that two is Prime and all other even values are composite
    #values
    if p == 2:
        return True
    elif (not p&1):
        return False
    
    for x in range(0, accuracy):
        a = random.randint(2, p-1)
        
        res = modexp(a, p-1, p)
        
        if res == 1:
            continue
        else:
            return False
        
    return True

def genprime(binbytes = 8, accuracy = 100):
    isPrime = False
    
    tries = 0
    
    while(not isPrime):
        tries+=1
        a = int.from_bytes(os.urandom(binbytes), 'little')
            
        isPrime = primality(a, accuracy)
        # I wanted to track how many probes I had to 
        # make to find a prime
        #if (tries%1000 ==0):
            #print(tries)
    
    return (a, tries)

def PiFunc(x):
    #input: An Integer value
    #output: an estimate on the number of primes less than x
    return x/math.log(x)

#sill bunk...
def EstimatedChecks(binBytes):
    largest = math.pow(2,binBytes)-1
    smallest = math.pow(2, binBytes-1)
    ourRange = largest #- smallest;
    
    probability = PiFunc(largest)#(PiFunc(largest)-PiFunc(smallest))
    probability /= ourRange
    probability *= 100
    return probability

# in progress
def RSAKey(binBytes):
    p = genprime(binBytes)
    q = genprime(binBytes)
    N = p*q
    
    e = gcd(p-1, q-1)
    (d, toss, temp) = egcd(e, N)
    
    return N, e, d
    

def main():
    random.seed()
    avgRunTime = 0
    avgTries = 0
    
    # How many times do I want to generate a large random prime
    numRuns = 1
    # How many bytes should the prime be made up of.
    numbytes = 64
    # How accurate do I want my primality test. I di
    accuracy = 100
    
    print("Estimated ", EstimatedChecks(numbytes), "% chance of picking Prime.")
    
    #now lets try and generate a large number.
    for i in range(0, numRuns):
        #start stop watch for this run
        startTime = time.time()
        
        #calculate a prime number and print it when found
        (prime, tries) = genprime(numbytes, accuracy)
        print(prime)
        
        #Stop watch for this run
        endTime = time.time();
        
        avgTries += tries
        avgRunTime += endTime-startTime
        
    avgRunTime /= numRuns
    avgTries //= numRuns
    print("Average Run Time Per Prime: ", avgRunTime)
    print("Average Tries Per Prime: ", avgTries)
    
main()
