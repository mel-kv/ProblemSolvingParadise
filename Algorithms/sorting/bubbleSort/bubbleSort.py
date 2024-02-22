def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i -1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        j += 1
    i += 1
  return arr


a = [3, 6, 7, 1, 5, 4, 68, 4, 2]


print(bubbleSort(a))


'''
Bubble Sort algorithm - a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The function bubbleSort(arr) takes a list arr as an input and returns the sorted list. 

When two elements are of equal value, a stable sorting algorithm preserves the elements’ relative order — the element’s relative position in the output will be the same as in the input. The bubble sort algorithm is stable, as it does not swap elements that have the same value.

An algorithm is called in-place when it only needs a constant amount of extra space to produce the desired output. We know that the bubble sort algorithm’s space complexity is O(1). Therefore, bubble sort is an in-place sorting algorithm.

With each pass in bubble sort, adjacent elements that are not in the correct order get swapped. Basically, elements greater than their adjacent elements “bubble up” or move towards their proper position with each pass. Hence the name “bubble” sort.
'''