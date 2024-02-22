const diff = (arr1, arr2) => [
  ...arr1.filter(e => !arr2.includes(e)),
  ...arr2.filter(e => !arr1.includes(e))
];

const sym = (...args) => {
  const reducedArgs = args.reduce(diff)
  return [...new Set(reducedArgs)]; 
   
}

let result = sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]).sort();

console.log(result) 



// diff function:

// This function takes two arrays (arr1 and arr2) as input and returns an array containing the symmetric difference between them.
// It uses the spread operator (...) along with the filter method to filter out elements that are not present in both arrays. This is done by filtering elements that are in one array but not in the other.
// The result is an array containing elements that are unique to either arr1 or arr2.



// sym function:

// This function takes any number of arrays (...args) as input and computes the symmetric difference of all the arrays.
// It utilizes the reduce method along with the diff function defined earlier to compute the symmetric difference iteratively across all arrays.
// The Set constructor is then used to remove duplicate elements from the result array, and the spread operator (...) is used to convert the set back into an array.

