# Sieve of Eratosthenes



def primes(n):
  range_number = n + 1
  numbers = [[p, True] for p in (range(2, range_number))]
  for i, num in enumerate(numbers):
    if (range_number) ** (1/2) >= num[0]:
      if num[1] == True:
        for rest_n in numbers[i+1:]:
          if rest_n[0] % num[0] == 0:
            rest_n[1] = False
    else:
      break
          
  return [p[0] for p in numbers if p[1]== True]


print(primes(100))


'''
Sieve of Eratosthenes

HOW IT WORKS:

Initialization: The function starts by creating a list named numbers, where each element is a list [p, True]. p ranges from 2 to n (inclusive), representing potential prime numbers. Each number is initially marked as True, indicating it is presumed to be prime.

Sieve Process:

The function iterates over numbers using enumerate, which provides both the index (i) and the value (num) of each item. The value num is itself a list where num[0] represents the potential prime number, and num[1] represents whether it is still considered prime (True) or has been marked as not prime (False).
It checks if the square root of the range (range_number), which is n + 1, is greater than or equal to the current number (num[0]). This comparison uses the mathematical principle that if a number is not divisible by any prime number less than or equal to its square root, it is prime.
For each number that passes this check and is still marked as True, the code iterates over the subsequent numbers in the list (numbers[i+1:]). If any of these numbers are divisible by num[0], they are marked as not prime (False) by setting rest_n[1] = False.

Filtering Primes:

After iterating through all numbers and marking non-primes, the function compiles a list of numbers that are still marked as True (prime) by filtering numbers based on p[1] being True.
It returns this list, which contains only the prime numbers up to n.

Output:

Finally, calling print(primes(100)) outputs the prime numbers up to 100.

'''