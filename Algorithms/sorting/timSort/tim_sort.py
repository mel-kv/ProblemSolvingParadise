def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []

    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    min_run = 32

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min((start + size - 1), (n - 1))
            end = min((start + 2 * size - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2

    return arr


# Example usage:
arr = [3, 6, 7, 1, 5, 4, 68, 4, 2]
sorted_arr = tim_sort(arr)
print(sorted_arr)


'''
Tim Sort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort, designed to perform well on many kinds of real-world data. It was implemented by Tim Peters for use in the Python programming language's built-in sorting functionality. Tim Sort is efficient for both small and large datasets and is particularly effective when dealing with partially ordered arrays or arrays with multiple runs of sorted elements.

The choice of the minimum run length in Tim Sort is based on empirical studies and performance considerations. A minimum run length of 32 is a common choice because it balances several factors to achieve good performance:

Insertion Sort Efficiency: Insertion Sort is efficient for small arrays or small runs of elements. By setting the minimum run length to 32, Tim Sort ensures that Insertion Sort is applied to relatively small sections of the array. This helps to minimize the overhead of using Insertion Sort while still taking advantage of its efficiency for small arrays.

Merge Sort Efficiency: Merge Sort is efficient for larger arrays or larger runs of elements. By dividing the array into runs of at least 32 elements, Tim Sort ensures that Merge Sort is applied to reasonably sized sections of the array. This allows Merge Sort to efficiently sort larger portions of the array.

Overall Algorithm Performance: The choice of 32 as the minimum run length strikes a balance between the efficiency of Insertion Sort for small arrays and the efficiency of Merge Sort for larger arrays. It has been found through experimentation that this value generally leads to good overall performance across a wide range of input data.

Trade-offs: While smaller or larger minimum run lengths may work well for specific types of input data, a value of 32 is often chosen as a practical compromise that performs well across different scenarios.

'''