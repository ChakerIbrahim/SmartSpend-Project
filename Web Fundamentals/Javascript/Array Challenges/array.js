function alwaysHungry(arr) {
    let foundFood = false;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("Yummy");
            foundFood = true;
        }
    }

    if (!foundFood) {
        console.log("I'm Hungry");
    }
}


alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4,1,5,7,2]);
//higher more than the target//
function highPass(arr, cutoff) {
    let result = [];
    for (i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            result.push(arr[i]);
        }
    }
    return result;
}
let x = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(x);
//BetterThanAverage//
function betterThanaverage(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    let average = sum / arr.length
    let count = 0
    for (i = 0; i < arr.length; i++) {
        if (arr[i] > average) {
            count++
        }
    }
    return count;
}
let result = betterThanaverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);
// Array Reverse//
function reverese(arr) {
    let results = [];
    for (let i = arr.length - 1; i >= 0; i--) {
       results.push(arr[i]);
    }
    return results;
}
let result2 = reverese(["a", "b", "c", "d", "e"]);
console.log(result2);

function fibonacciArray(n) {
    var fibArr = [0, 1];
    for(var i = 2;i < n ;i++){
        fibArr.push(fibArr[i - 1] + fibArr[i - 2]);
    }
    return fibArr;
   
}
   
var result3 = fibonacciArray(10);
console.log(result3); 


