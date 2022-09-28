"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    number = 2
    
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be greater than 0")

    while count < number_of_primes:
         prime = True
         for i in range(2, number):
             if number % i == 0:
                 prime = False
                 break
         if prime:
             list.append(number)
             count += 1
         number += 1
    return list
