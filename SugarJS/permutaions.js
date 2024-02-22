// A permutation is a rearrangement of the elements of a set or sequence into a particular order. In other words, given a collection of items, a permutation is any possible arrangement of those items. The number of permutations of a set of n elements is denoted by n!.

// For example, consider the set {1, 2, 3}. The permutations of this set are:

// {1, 2, 3}
// {1, 3, 2}
// {2, 1, 3}
// {2, 3, 1}
// {3, 1, 2}
// {3, 2, 1}

// Each of these arrangements is a permutation of the original set. Permutations are commonly used in various fields such as mathematics, computer science, and combinatorics. They are often employed in algorithms and problems involving the arrangement of elements or objects in a specific order.



// Function to check if a permutation has consecutive repeated characters
function hasConsecutiveRepeats(permutation) {
  // Regular expression to match consecutive repeated characters
  const regex = /(.)\1+/;
  // Test if the permutation contains consecutive repeated characters
  return !regex.test(permutation);
}

// Function to generate permutations using backtracking
function generatePermutations(arr, start, end, result) {
  // Base case: If we've reached the end of the array, check for consecutive repeats and add to result
  if (start === end) {
      if (hasConsecutiveRepeats(arr.join(''))) {
          result.push([...arr]);
      }
      return;
  }

  // Generate permutations by swapping characters
  for (let i = start; i <= end; i++) {
      // Swap characters at positions start and i
      [arr[start], arr[i]] = [arr[i], arr[start]];

      // Recursively generate permutations for the remaining characters
      generatePermutations(arr, start + 1, end, result);

      // Undo the swap to backtrack
      [arr[start], arr[i]] = [arr[i], arr[start]];
  }
}

// Function to count permutations without consecutive repeated characters
function countPermutationsWithoutConsecutiveRepeats(str) {
  // Convert the input string into an array of characters
  const chars = str.split("");
  // Initialize an empty array to store the final permutations without consecutive repeated characters
  const permutations = [];

  // Generate permutations using backtracking
  generatePermutations(chars, 0, chars.length - 1, permutations);

  // Return the count of permutations without consecutive repeated characters
  return permutations.length;
}

// Example usage:
const inputString = "abcdefa";
const result = countPermutationsWithoutConsecutiveRepeats(inputString);
console.log(`The number of permutations of "${inputString}" without consecutive repeated characters: ${result}`);
