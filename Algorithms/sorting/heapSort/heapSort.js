function heapify(arr, n, i) {
  let largest = i;
  let left = 2 * i + 1;
  let right = 2 * i + 2;

  if (left < n && arr[largest] < arr[left]) {
      largest = left;
  }
  if (right < n && arr[largest] < arr[right]) {
      largest = right;
  }
  if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]]; // Swap
      heapify(arr, n, largest);
  }
}

function heapSort(arr) {
  const n = arr.length;

  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
      heapify(arr, n, i);
  }

  for (let i = n - 1; i > 0; i--) {
      [arr[i], arr[0]] = [arr[0], arr[i]]; // Swap
      heapify(arr, i, 0);
  }

  return arr;
}

const a = [3, 6, 7, 1, 5, 4, 68, 4, 2];
console.log(heapSort(a));
