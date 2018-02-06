var arr1 = ['string 1','string 3', 'str5','str7', 'string 9'];
var arr2 = ['str 2','string 3', 'Str6','str7', 'strin10', 'string 12'];
console.log('arr1 = ', arr1);
console.log('arr2 = ', arr2);
var arrJoined = arr1.concat(arr2);
console.log('After joining...');
console.log('arrJoined = ', arrJoined);
var arrSorted = [...arrJoined];
arrSorted.sort();
console.log('After sorting...');
console.log('arrSorted = ', arrSorted);
var arrWithoutDuplicates = Array.from(new Set(arrJoined));
console.log('After deleting duplicates...');
console.log('arrWithoutDuplicates = ', arrWithoutDuplicates);
var arrFiltered5Plus = arrWithoutDuplicates.filter (function(element) {
    return element.length >= 5;
});
console.log('After filtering 5+ symbols');
console.log('arrFiltered5Plus = ', arrFiltered5Plus);
var arrPlusCode = arrJoined.map(x=>'CODE ' + x);
console.log('After adding \'CODE\' to each element');
console.log('arrPlusCode = ', arrPlusCode);


///[\w]+(?=\'? is[not]? applied| is not valid)/


