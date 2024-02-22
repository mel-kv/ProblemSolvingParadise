def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
  n = len(arr)
  last_non_leaf_node = n // 2 - 1
  for i in range(last_non_leaf_node, -1, -1):
      heapify(arr, n, i)
  for i in range(n - 1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i]  # Swap
      heapify(arr, i, 0)
  return arr

a = [3, 6, 7, 1, 5, 4, 68, 4, 2]

print(heapSort(a))

'''
Heap Sort - a popular sorting algorithm that operates in two main phases: building a heap from the input array and then sorting the array by repeatedly extracting the maximum element from the heap and adjusting the heap accordingly. The brilliance of heapification lies in the following fact:
If all the subtrees in a binary tree are MaxHeaps themselves, the whole tree is a MaxHeap. 

HOW IT WORKS:

Function: heapify(arr, n, i):
This function is responsible for maintaining the heap property in a subtree with root at index i in an array arr of size n. The heap property is that for every node i other than the root, the value of i is not greater than the value of its parent. This particular implementation ensures a max heap, where the parent node is greater than or equal to its children.

Parameters:
arr: The array representing the heap.
n: The number of elements in arr that should be considered part of the heap.
i: The index of the root of the subtree being heapified.

Process:
The function starts by assuming that the largest element is the root of the subtree (largest = i).
It calculates the indices of the left (2 * i + 1) and right (2 * i + 2) children of the root.
It compares the root with its left child; if the left child is larger, it updates largest to be the left child's index.
It then compares the largest element (either the root or the left child, after the previous step) with the right child; if the right child is larger, it updates largest to be the right child's index.
If the largest element is not the root (meaning either child was larger than the root), it swaps the root with the largest element and recursively heapifies the affected subtree to maintain the heap property.


Function: heapSort(arr)
This function sorts an array arr using the Heap Sort algorithm.

Process:
Building a Max Heap: It first builds a max heap from the unsorted input array. This is done by calling heapify for all non-leaf nodes of the heap (nodes from n // 2 - 1 to 0). Leaf nodes already satisfy the heap property and don't need to be heapified.

Sorting: 
Once the max heap is built, the function repeatedly swaps the first element of the array (which is the maximum element in the heap) with the last element in the unsorted portion of the array, then reduces the size of the heap by one (effectively removing the maximum element from the heap). After each swap, it calls heapify on the root of the heap to ensure the max heap property is maintained for the remaining elements. This process is repeated until all elements are sorted.

Sorting the Example Array a: 
When heapSort is called with the example array a = [3, 6, 7, 1, 5, 4, 68, 4, 2], it first transforms the array into a max heap and then sorts it by repeatedly extracting the maximum element and adjusting the heap.


Heap does not always need to be a binary tree. But in heap sort, we use arrays to represent the heap. Using the array, we can easily calculate and track the relationship between a parent index, its left child index, and the right child index for a binary heap. And a binary heap has to be binary-tree-based.

While heap sort is typically not stable, it can be made stable by considering the position of the elements with the same value. During heapification, treat the element towards the right as greater than the element towards the left, and your sorting will be stable. 

Storing and accessing values in an array is faster and less complicated than using a more complex data structure. One of the main advantages of using more complex data structures is the use of methods provided by the standard library for common operations related to the data structure, e.g., push() and pop() methods for a stack. 
However, storing a complete binary tree in an array still allows us to perform all operations relevant to the tree with much ease. We can find the left child, right child, parent node, root, and the last element of a tree with basic arithmetic operations on the index of the current node or the variable maintaining the size of the tree.

The maximum element is present at the root and can be found in O(1) time. The minimum element will be present in the leaf nodes, and all leaf nodes have to be checked to find the minimum element. Hence, the minimum element can be found in O(n) time.

Heap sort’s space complexity is a constant O(1) due to its auxiliary storage.

'''