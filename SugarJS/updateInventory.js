function updateInventory(arr1, arr2) {
  for (let index = 0; index < arr2.length; index++) {
    let qty = arr2[index][0]
    let product = arr2[index][1]
    let match = false; 
    for (let i = 0; i < arr1.length; i++) {
      const element = arr1[i];
      if (element[1] === product) {
        element[0] += qty;
        match = true;
        break;
      }
    }
    if (!match) {
      arr1.push([qty, product]);
    }
  }
  

  arr1.sort((a, b) => a[1].localeCompare(b[1]));
  
  return arr1;
}

let result = updateInventory([
  [0, "Bowling Ball"], 
  [0, "Dirty Sock"], 
  [0, "Hair Pin"], 
  [0, "Microphone"]
], [
  [1, "Hair Pin"], 
  [1, "Half-Eaten Apple"], 
  [1, "Bowling Ball"], 
  [1, "Toothpaste"]
]);

console.log(result);


