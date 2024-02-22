def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    pivot_index = partition(arr, left, right)
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)

    return arr

def partition(arr, left, right):
    pivot_value = arr[right]
    partition_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, partition_index)
            partition_index += 1

    swap(arr, right, partition_index)
    return partition_index

def swap(arr, first_index, second_index):
    arr[first_index], arr[second_index] = arr[second_index], arr[first_index]


a = [3, 6, 7, 1, 5, 4, 68, 4, 2]
sorted_a = quick_sort(a)
print(sorted_a)

'''
Quick Sort algorithm - Quicksort is one of the most efficient and commonly used sorting algorithms. It is a divide-and-conquer algorithm. It’s also an in-space algorithm as it does not use any extra space for sorting the input data, unlike the merge sort algorithm.  Rearranges the elements within the array without using additional arrays for the smaller and larger elements relative to the pivot. 

HOW IT WORKS:

Quicksort implementation requires two main methods:

quickSort(): Selects a pivot element, partitions the array around the pivot element, and recursively sorts the partitioned subarrays.

partition(): Assigns the pivot element and places the pivot element at its right position in the sorted array. Then, it places all smaller elements to the left of the pivot and places all larger or equal elements to the pivot’s right.

Base Condition: 
If the right index is None, it's set to the last index of arr. The function returns if the left index is not smaller than the right index, indicating that the partition size is 1 or 0.

Partitioning: 
The partition function arranges the elements of arr such that all elements less than a chosen pivot value are moved before it, and all greater elements are moved after it. The pivot's final position is its correct position in the sorted array.

Recursive Calls: 
quick_sort is then recursively called on the sub-arrays to the left and right of the pivot's final position.

Swapping: 
The swap function exchanges the values of two elements in arr.

Efficient implementation of quicksort is not stable because it swaps non-adjacent elements, and the relative order of equal array elements may change. Quicksort can be made stable, but it will require extra O(n) space.
'''


def quick_sort_cheat_mode(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_cheat_mode(left) + middle + quick_sort_cheat_mode(right)


b = [3, 6, 7, 1, 5, 4, 68, 4, 2]
sorted_b = quick_sort_cheat_mode(a)
print(sorted_b)


'''
Quick Sort - Cheat Mode algorithm - more Pythonic, but less space-efficient version, often referred to as "cheat mode" due to its simplicity and reliance on list comprehensions for partitioning.. 

HOW IT WORKS:

Base Condition: 
Returns the array if its length is 0 or 1 (already sorted).

Partitioning: 
Uses list comprehensions to create left and right arrays containing elements less than and greater than the pivot, respectively. The pivot is the first element of arr.

Recursive Calls and Concatenation: 
Recursively applies quick_sort (the traditional version, though likely intended to be quick_sort_cheat_mode) to left and right, then concatenates the sorted left, pivot, and sorted right into a single array.
'''