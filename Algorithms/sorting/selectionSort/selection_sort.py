def selectionSort(arr):
  for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    if min != i:
      arr[i], arr[min] = arr[min], arr[i]
    
  return arr



a = [3, 6, 7, 1, 5, 4, 68, 4, 2]

print(selectionSort(a))


'''
HOW IT WORKS:

Selection sort works by selecting the smallest element from an unsorted list and moving it to the front. We'll scan through all the items (from left to right) to find the smallest one and move it to the front. Now, the first item is sorted, and the rest of the list is unsorted. Repeat! We'll look through all the unsorted items, find the smallest one, and swap it with the first unsorted item. We can do this for the next-smallest item and so on. 


The Selection Sort algorithm has a time complexity of O(n^2), where 'n' is the number of elements in the array. Despite its simplicity, it is not very efficient, especially for large arrays, as it performs a large number of comparisons and swaps. However, it has the advantage of requiring only O(1) additional space, making it suitable for situations where memory usage is a concern.

The selection sort algorithm is an in-place, comparison-based sorting algorithm. This basically means that this algorithm transforms a given input (in this case, an array) without using any other data structure. In such cases, the input is usually overwritten by the output.

The selection sort algorithm makes n-1 swaps in the worst case and zero swaps in the best case. Therefore, it never makes more than O(n) swaps. So, it is handy in situations where “memory write” is a costly operation.

'''