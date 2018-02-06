function findCoupons(elements_arr) {
    let found_codes = [];
    elements_arr.forEach(function(element){
      let string = element.innerHTML;
      if (string.match(/[\w]+(?= is not applied|\'? is applied| is not valid)/)) {
          found_codes.push(string.match(/[\w]+(?= is not applied|\'? is applied| is not valid)/g)[0]);
      }
    });
    return found_codes;
}

var pricesText = document.querySelector('#main-content > div.table-wrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > ul > li:first-child').innerHTML;
var prices = pricesText.replace(/\,/g,'').match(/\d+[\.\d]*/g);
console.log('prices = ', prices);
  
var codes = [];
codes = codes.concat(findCoupons(document.querySelectorAll(".codes-wrapper span")));
//document.querySelector(".styles--coupon-box__attempt--3xvRr").prev("p").addClass(".styles--coupon-box__attempt--3xvRr"); 
codes = codes.concat(findCoupons(document.querySelectorAll(".confluenceTd > ul:first-child ~ p"))).sort();
console.log('codes =', codes);

// I tried with /[\w]+(?=\'? is[not]? applied| is not valid)/ - doesn't work