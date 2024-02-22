# Dijkstra's Prime Algorithm

def show_prime_numbers_in(n):
  pool = {2:4, }
  for number in range(3, n+1):
    min_n = min(pool.values())
    if number < min_n:
      pool[number] = number ** 2
    else:
      for k, v in pool.items():
        if v == min_n:
          pool[k] = v + k
  return list(pool.keys())


print(show_prime_numbers_in(100))


'''
Dijkstra's Prime Algorithm

HOW IT WORKS:

Initialization: The function starts by initializing pool with {2: 4}, setting the foundation for the algorithm with the first prime number, 2, and its square as the value.

Iteration Through Range: It iterates through the range from 3 to n (inclusive), applying a unique mechanism to manage and update pool.

Minimum Value Determination: For each iteration, the function finds the minimum value in pool, which initially is 4 (the square of 2).

Condition and Update Logic:

If the current number is less than the minimum value found in pool, it adds the number to pool with its square as the value. This condition aims to capture new 'prime-like' numbers and their squares.
If the current number is not less than the minimum value, it searches for keys in pool whose value matches this minimum value and updates their value by adding the key to it. This step is intended to incrementally adjust the values associated with each key based on the algorithm's logic.
Return Statement: Finally, the function returns a list of keys from pool, which represents the numbers identified by this custom algorithm.

Return Statement: 

Finally, the function returns a list of keys from pool, which represents the numbers identified by this custom algorithm.

'''

