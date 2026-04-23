function alwaysHungry(arr) {
    if (arr.includes("food")) {
        console.log("yummy")
    }
    else {
        console.log("I'm Hungry")
    }
}
alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([1, 2, 5, 7, 8]);
/////
function highPass(arr, cutoff) {
    let result = [];
    for (i = 0; i < arr.length; i++) {
        if(arr[i] > cutoff){
            result.push(arr[i]);
        }
    }

    return result;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);
////
function reverse(arr) {
    let result = [];
    for (i = arr.length - 1; i >= 0; i--) {
        result.push(arr[i]);
    }
    return result;
}
let result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);