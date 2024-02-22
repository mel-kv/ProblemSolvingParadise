function quickSort(arr, left = 0, right = arr.length - 1) {
  if (left >= right) {
    return;
  }

  let pivotIndex = partition(arr, left, right);
  quickSort(arr, left, pivotIndex - 1);
  quickSort(arr, pivotIndex + 1, right);

  return arr;
}

function partition(arr, left, right) {
  let pivotValue = arr[right];
  let partitionIndex = left;

  for (let i = left; i < right; i++) {
    if (arr[i] < pivotValue) {
      swap(arr, i, partitionIndex);
      partitionIndex++;
    }
  }

  swap(arr, right, partitionIndex);
  return partitionIndex;
}

function swap(arr, firstIndex, secondIndex) {
  let temp = arr[firstIndex];
  arr[firstIndex] = arr[secondIndex];
  arr[secondIndex] = temp;
}


function quickSortCheatMode(arr) {
  if (arr.length <= 1) return arr;
  let pivot = arr[0];
  let left = arr.filter(x => x < pivot);
  let right = arr.filter(x => x > pivot);
  return [...quickSort(left), pivot, ...quickSort(right)]
}




var a = [3, 6, 7, 1, 5, 4, 68, 4, 2]
quickSort(a)




