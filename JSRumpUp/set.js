const arr1 = [1, "2", 23, "2"];
const arr2 = [1, 2, 23, "2"];
var set = new Set (arr1.concat(arr2));
console.log('set = ', set);
var returnedArr = Array.from(set);
console.log('returnedArr= ', returnedArr);