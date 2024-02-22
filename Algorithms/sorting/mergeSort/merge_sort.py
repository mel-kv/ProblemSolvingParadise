def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    arr = []
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))

    return arr + left + right




a = [3, 6, 7, 1, 5, 4, 68, 4, 2]
print(mergeSort(a))


"""
Merge Sort algorithm - an efficient, general-purpose, comparison-based sorting algorithm. Merge Sort is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used to merge two halves. The mergeSort(arr) function recursively splits the list until it consists of lists of less than two elements (which are trivially sorted) and then merges those sorted lists back together in order.

HOW IT WORKS:

Base Condition:
If the list arr has fewer than two elements, it's returned as is because a list with 0 or 1 element is already sorted.

Dividing the Array:
The array is divided into two halves using the mid index.
left contains the first half of arr, and right contains the second half.

Recursive Calls:
mergeSort is called recursively for the left and right halves of the array.

Merging:
The merge() function takes two sorted lists, left and right, and merges them into a single sorted list. It compares the first elements of each list, appending the smaller one to the result list arr, and removes it from its original list using pop(0). This process is repeated until one of the lists is empty. Finally, if any elements are left in left or right (because one list was longer than the other), they are added to arr. Since left and right are already sorted, appending them directly to arr maintains the sorted order.

An in-place algorithm processes the input and produces the output in the same memory location that contains the input without using any auxiliary space. However, a small extra space for variables is allowed. And so, merge sort is not an in-place sorting algorithm, because we use an auxiliary array to hold the merged list temporarily.

A sorting algorithm is said to be stable if the order of any two equal elements in the original list and the sorted list stays the same. It depends on how we implement the algorithm. Most implementations of this algorithm produce a stable sort. While merging the left and the right list, if the first element of both lists are equal, select the element from the left list. This will produce a stable sort. Otherwise, the algorithm will not produce a stable sort.

"""