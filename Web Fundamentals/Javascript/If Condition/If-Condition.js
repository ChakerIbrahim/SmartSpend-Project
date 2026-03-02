let number = 10;
if (number > 0){
    console.log("Positive Number");
}
else if (number < 0) {
    console.log("Negative Number")
}
else {
    console.log("Number is zero")
}

let time = new Date().getHours(); 
if (time < 12){
    console.log("Good morning");
}
else {
    console.log("Good Afternoon");
}

let grade = 88;
if(grade >= 90){
    console.log("A");
}
else if(grade>=80 && grade<=89) {
console.log("B")
}
else if(grade >=70 && grade <=79) {
    console.log("C")
}
else {
    console.log("F")
}
let day = "Sunday";
if (day == "Friday" || day == "Saturday" ){
    console.log("Weekend");
}
else{
    console.log("Weekday");
}
