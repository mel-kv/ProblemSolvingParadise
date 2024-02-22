export function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) { 
    let min = i; 
    for (let j = i + 1; j < arr.length; j++) { 
      if (arr[j] < arr[min]) {
        min = j;   
      }
    }
    if (min !== i) {
      [arr[i], arr[min]] = [arr[min], arr[i]]; 
    }
  }
  return arr; 
}


var a = [3, 6, 7, 1, 5, 4, 68, 4, 2]
selectionSort(a)
