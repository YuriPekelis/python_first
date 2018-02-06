
const bestCodeText = 'bestCode';
const bestCodeDiscountText = 'bestCodeDiscount';
const originalPriceText = 'originalPrice';
var result = [];
var codes = new Object(); //new Map();
var bestCode = new Object(); //new Map();
var originalPrice = new Object(); //new Map();

function parsePrice(text, reg_val) {
  return parseFloat(text.match(reg_val)[0].replace(/\,/g,''));
}
originalPrice[originalPriceText] = parsePrice(document.querySelector(".total-wrapper").innerText, /[\d\,\.]+/);

document.querySelectorAll(".codes-wrapper li").forEach(function(element){
    let string = element.innerText;
    let key = string.match(/(?<=Code \').*(?=\' is)/)[0];
    let currentDiscount = originalPrice[originalPriceText] - parsePrice (string, /(?<=is: )[\d\,\.]*/);
    if (bestCode[bestCodeDiscountText] === undefined || currentDiscount > bestCode[bestCodeDiscountText]) {
        bestCode[bestCodeText] = key;
        bestCode[bestCodeDiscountText] = currentDiscount;
    }
    codes[key] = currentDiscount;
});
result.push(codes);
result.push(bestCode);
result.push(originalPrice);
console.log(result);



