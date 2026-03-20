//reverse String//
function reverseString(str) {
    var result = "";

    for (var i = str.length - 1; i >= 0; i--) {
        result += str[i];
    }

    return result;
}

console.log(reverseString("creature")); 

//Remove EVEN Strings//
function keepOddStrings(arr) {
    var result = [];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length % 2 !== 0) {
            result.push(arr[i]);
        }
    }

    return result;
}
console.log(keepOddStrings(["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."]));

//Integer to ROMAN NUMERALS //
function intToRoman(num) {
    var values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    var symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    var result = "";

    for (var i = 0; i < values.length; i++) {
        while(num >= values[i]) {
            result += symbols[i];
            num -= values[i];
        }
    }

    return result;
}
console.log(intToRoman(444)); 
console.log(intToRoman(349)); 
console.log(intToRoman(58)); 

//digit by digit//
function intToRoman(num) {
    var thousands = ["", "M", "MM", "MMM"];
    var hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    var tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    var ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

    return (
        thousands[Math.floor(num / 1000)] +
        hundreds[Math.floor((num % 1000) / 100)] +
        tens[Math.floor((num % 100) / 10)] +
        ones[num % 10]
    );
}
console.log(intToRoman(1122));

//Roman to integer//
function romanToInt(roman) {
    var map = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };

    var sum = 0;

    for (var i = 0; i < roman.length; i++) {
        if (map[roman[i]] < map[roman[i + 1]]) {
            sum -= map[roman[i]];
        } else {
            sum += map[roman[i]];
        }
    }

    return sum;
}
console.log(romanToInt("I"));    
console.log(romanToInt("IV"));     
console.log(romanToInt("IX"));     
console.log(romanToInt("M"));  
console.log(romanToInt("XVI"));   
console.log(romanToInt("III"));  
console.log(romanToInt("MCMXCV"));
