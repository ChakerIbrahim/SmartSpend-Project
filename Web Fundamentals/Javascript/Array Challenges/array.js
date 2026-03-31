function alwaysHungry(arr) {
    let foundFood = false;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("Yummy");
            foundFood = true;
        }
    }

    if (foundFood === "food") {
        console.log("I'm Hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);

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


