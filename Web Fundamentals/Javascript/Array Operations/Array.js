/* --- Accessing Elements ---*/
let colors = ["red", "blue", "green", "yellow", "purple"];
console.log(colors[0]);  /* First Elements */
console.log(colors[colors.length - 1]);  /*Last Elements */
console.log(colors[1]); /*Second  Elements*/
colors[2] = "orange";    /*Update the third Element to Orange*/
console.log(colors);

/* --- Traversing Array --- */
let numbers = [10, 20, 30, 40, 50];    /*Print Elements Normally*/
for (i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

for (i = numbers.length - 1; i >= 0; i--) { /*print Elements in reverse*/
    console.log(numbers[i]);
}

/* --- Searching in an array --- */
let arrays = [5, 10, 15, 20, 25];
if (arrays.indexOf(25) !== -1) {
    console.log("found at Position" + " " + arrays.indexOf(25))
}
else {
    console.log("Not Found")
}

/* --- Sorting an Array --- */

/*Ascending Order*/
let scores = [50, 20, 70, 10, 40];
scores.sort(function (a, b) {
    return a - b;
});
console.log(scores);
/*Descending Order*/
scores.sort(function (a, b) {
    return b - a;
});
console.log(scores);

/*Sort alphabetical order*/
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
console.log(names.sort());

/* Inserting Elements*/
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant");  //Add Element at the end
console.log(animals);
animals.unshift("Lion");  //Add element at the beginning of array
console.log(animals);
animals.splice(2, 0, "tiger")  //insert element between elements
console.log(animals);

/* ---Deleting Elements---*/
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift();    //remove From the first of array
console.log(fruits);
fruits.pop()      //remove from the end
console.log(fruits);
let index = fruits.indexOf("banana")
fruits.splice(index, 1);
console.log(fruits);

/*---Combining Arrays---*/
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let combined = [];
for (i = 0; i < array1.length; i++) {
    combined.push(array1[i]);
}
for (i = 0; i < array2.length; i++) {
    combined.push(array2[i])
}
console.log(combined);

/*---Splitting an Array---*/
let items = ["a", "b", "c", "d", "e"];
firstpart = items.slice(0, 3);
secondpart = items.slice(3);
console.log(firstpart);
console.log(secondpart);

/*---Filtering Elements---*/
let number = [1, 5, 10, 15, 20, 25, 30];
for (i = 0; i < number.length; i++) {
    if (number[i] > 15) {
        console.log(number[i])
    }
}

/*remove duplicate elements from an array*/
let nums = [1, 2, 2, 3, 4, 4, 5];
let duplicateElement = [];
for (i = 0; i < nums.length; i++) {
    if (!duplicateElement.includes(nums[i])) {
        duplicateElement.push(nums[i]);
    }
}
console.log(duplicateElement);

/*Bonus Challenge*/
let arr1 = [1, 3, 5];
let arr2 = [2, 4, 6];
let merged = [...arr1, ...arr2];
for (i = 0; i < merged.length; i++) {
    for (j = i + 1; j < merged.length; j++) {
        if (merged[i] > merged[j]) {
            let temp = merged[i];
            merged[i] = merged[j];
            merged[j] = temp;
        }
    }
}
console.log(merged);