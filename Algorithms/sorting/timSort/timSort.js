function insertionSort(arr, left = 0, right = null) {
  if (right === null) {
      right = arr.length - 1;
  }

  for (let i = left + 1; i <= right; i++) {
      let key = arr[i];
      let j = i - 1;
      while (j >= left && arr[j] > key) {
          arr[j + 1] = arr[j];
          j--;
      }
      arr[j + 1] = key;
  }

  return arr;
}

function merge(arr, l, m, r) {
  let len1 = m - l + 1;
  let len2 = r - m;
  let left = [];
  let right = [];

  for (let i = 0; i < len1; i++) {
      left.push(arr[l + i]);
  }
  for (let i = 0; i < len2; i++) {
      right.push(arr[m + 1 + i]);
  }

  let i = 0, j = 0, k = l;
  while (i < len1 && j < len2) {
      if (left[i] <= right[j]) {
          arr[k] = left[i];
          i++;
      } else {
          arr[k] = right[j];
          j++;
      }
      k++;
  }

  while (i < len1) {
      arr[k] = left[i];
      i++;
      k++;
  }

  while (j < len2) {
      arr[k] = right[j];
      j++;
      k++;
  }
}

function timSort(arr) {
  const n = arr.length;
  const minRun = 32;

  for (let i = 0; i < n; i += minRun) {
      insertionSort(arr, i, Math.min(i + minRun - 1, n - 1));
  }

  let size = minRun;
  while (size < n) {
      for (let start = 0; start < n; start += 2 * size) {
          let mid = Math.min(start + size - 1, n - 1);
          let end = Math.min(start + 2 * size - 1, n - 1);
          merge(arr, start, mid, end);
      }
      size *= 2;
  }

  return arr;
}

// Example usage:
const arr = [5, 2, 8, 3, 6, 1, 9, 4, 7];
const sortedArr = timSort(arr);
console.log(sortedArr);
