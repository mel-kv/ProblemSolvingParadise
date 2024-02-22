def radix_sort(arr):
    max_digits = max([get_number_of_digits(num) for num in arr])
    for i in range(max_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = get_digit(num, i)
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr

def get_digit(num, place):
    return abs(num) // 10 ** place % 10

def get_number_of_digits(num):
    if num == 0:
        return 1
    return len(str(abs(num)))

a = [3, 61, 78, 1, 5, 4, 68, 4, 200, 457, 0, 4567]
sorted_a = radix_sort(a)
print(sorted_a)

"""
Radix Sort algorithm - an efficient non-comparison-based sorting algorithm that sorts numbers by processing individual digits. Radix Sort processes each digit of the numbers from the least significant digit to the most significant digit, grouping numbers by each digit's value during each pass through the array. This implementation handles positive integers and includes a mechanism to determine the maximum number of digits in the largest number, ensuring all numbers are processed through all their digits.

HOW IT WORKS:

Find the Maximum Number of Digits (max_digits):
The function get_number_of_digits is used to determine the number of digits in each number of the input list arr.
max_digits is set to the maximum number of digits found in any number within arr.

Sorting Process:
The sorting is done in max_digits passes. In each pass, the numbers are grouped based on the current digit being considered, starting from the least significant digit.
For each pass, buckets are prepared as a list of ten lists, each corresponding to a digit from 0 to 9.

Grouping into Buckets:
Each number in arr is placed into a bucket based on the current digit. The function get_digit extracts the digit from the number at the current place value (starting from the right, or least significant digit).
Numbers are collected from the buckets and concatenated back into arr, preserving the order within each bucket.

Extracting Digits:
get_digit calculates the digit at the given place value for a number, using division and modulo operations.
get_number_of_digits determines the total number of digits in a number, handling the special case where the number is 0.

Returning Sorted Array:
After all passes, arr is sorted by the least significant digit to the most significant digit, and the sorted array is returned.

Radix sort uses a stable sorting algorithm as its subroutine, preserving the relative order of two elements with the same key. Hence, radix sort is a stable sorting algorithm. (A sorting algorithm is stable if, for any two elements with the same key, the relative order of the two elements is preserved in the sorted output as it is in the original input.)

Since in radix sort, auxiliary data structures like arrays are used to sort the input array. The sorting process does not happen within the original array. Therefore, it is not an in-place sorting algorithm.

Radix sort and bucket sort are pretty similar; however, there’s one significant difference between the two. In bucket sort, sorting happens only from the most significant digit (MSD) to the least significant digit (LSD). On the other hand, in radix sort, the implementation can go from MSD to LSD or LSD to MSD — there’s no restriction.

"""