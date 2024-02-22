def insertionSort(arr):
  for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    while (j > -1) and (current < arr[j]):
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = current
  return arr


a = [3, 6, 7, 1, 5, 4, 68, 4, 2]

print(insertionSort(a))

'''
Insertion Sort is a simple and efficient algorithm for sorting a small number of elements. It builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heap sort, or merge sort. However, its simplicity makes it easy to understand and implement for small datasets.

HOW IT WORKS:

Iterating Over the Array:
The algorithm iterates over the array starting from the second element (i = 1) to the last element. This is because the first element is considered to be in a "sorted portion" of the list.

Sorting Each Element:
For each iteration, the current element arr[i] is stored in current. This element will be inserted into its correct position in the already sorted portion of the array.
The index j is set to i - 1 to start comparing current with each element in the sorted portion (elements before i), moving backwards.

Finding the Correct Position for current:
A while loop is used to shift elements of the sorted portion that are greater than current one position to the right, to make space for inserting current into its correct position.
This shifting process continues as long as j > -1 (ensuring we're within the bounds of the array) and current < arr[j] (indicating that current has not yet reached its correct position).

Inserting current:
Once the correct position is found (or the beginning of the array is reached), current is inserted by setting arr[j+1] = current.


In a stable sorting algorithm, identical elements are sorted in the same order as they appear in the input array. In insertion sort, we insert the current element just after the element smaller than or equal to the current element, i.e., we stop shifting elements when we find an element smaller than or equal to the current element. Therefore, the order of equal elements in the unsorted array remains the same in the sorted array, making insertion sort stable.

An in-place algorithm is an algorithm that doesn’t use extra space for input manipulation. Its space complexity is usually less than linear. In Insertion sort, we only use a constant number of extra variables to store the current element, so the space complexity is O(1), making insertion sort an in-place sorting algorithm.

For sorting an array of size n through insertion sort, the total number of comparison operations is (n + the number of inversions in the array). The total number of pairs in an array is n * (n - 1) / 2.

Therefore, the maximum number of inversions possible
= n * (n - 1) / 2 (when the array is reverse-sorted)

The minimum of inversions = 0 (when the array is sorted) 

For a randomly arranged array, the average number of inversions
= the average of the maximum number of inversions and minimum number of inversions
= n * (n - 1) / 4

Therefore, the running time of insertion sort averages out to be quadratic, i.e., O(n2).
'''