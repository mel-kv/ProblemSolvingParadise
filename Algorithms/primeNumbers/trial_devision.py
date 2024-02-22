# Trial Division



def is_it_prime(number, primes):   
    max_prime = int(number ** (1/2))
    primes = [p for p in primes if p <= max_prime]
    for prime in primes:
        if (number % prime) == 0:
            return False
    return True


def show_prime_numbers_in(n):
    primes = []
    for number in range(2, n + 1):
        if is_it_prime(number, primes):
            primes.append(number)
    return primes


print(show_prime_numbers_in(100))


'''
Trial Division

HOW IT WORKS:

Function is_it_prime(number, primes)

Purpose: Determines if a given number is prime, using a list of already identified prime numbers primes.

Process:
Calculates max_prime, the square root of number, rounded down to the nearest integer. This is based on the mathematical fact that if a number is prime, it cannot be divisible by any number greater than its square root.
Filters the list primes to include only those primes that are less than or equal to max_prime. This optimizes the checking process, as any divisors larger than max_prime would not affect the primality of number.
Iterates through the filtered list of primes, checking if number is divisible by any of these primes. If number is divisible by any prime (remainder equals zero), it is not prime, and the function returns False.
If no divisors are found, the function concludes that number is prime and returns True.

Function show_prime_numbers_in(n)

Purpose: Generates a list of prime numbers up to (and including) a specified limit n.

Process:
Initializes an empty list primes to store the prime numbers found.
Iterates through each number from 2 to n (inclusive), as 1 is not considered a prime number.
For each number, it calls is_it_prime(number, primes) to check if the number is prime.
If is_it_prime returns True, indicating that number is prime, it appends number to the list primes.
After iterating through all numbers up to n, it returns the list primes, which now contains all prime numbers within the specified range.

'''
