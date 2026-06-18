// Remove Blanks //
function removeBlanks(str) {
    let newstring = "";
    for (i = 0; i < str.length; i++) {
        if (str[i] != " ") {
            newstring += str[i];
        }
    }
    return newstring;
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
console.log(removeBlanks("I can not BELIEVE it's not BUTTER"));

//get digits //
function getDigits(str) {
    var result = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] >= "0" && str[i] <= "9") {
            result += str[i];
        }
    }
    return Number(result);  //change it to number//
}
console.log(getDigits("abc8c0d1ngd0j0!8")); 

//Acronmys//
function acronym(str) {
    var words = str.split(" ");   //We divide the sentence into words//
    var result = "";
    for (var i = 0; i < words.length; i++) {
        var word = words[i];
        if (word.length > 0) {
            result += word[0].toUpperCase();
        }
    }
    return result;
}
console.log(acronym(" there's no free lunch - gotta pay yer way. "));
console.log(acronym("Live from New York, it's Saturday Night!"));

//Count Non-Spaces//
function countNonspaces(str){
    let result = 0;
    for(i = 0 ; i < str.length ; i++){
        if (str[i] !== " "){
            result++;
        }
    }
    return result;
}
console.log(countNonspaces("Honey pie, you are driving me crazy"));

// removeShorterStrings //
function  removeShorterStrings(arr,minlength){
    let result = [];
    for(i = 0;i <arr.length;i++){
        if (arr[i].length >= minlength){
            result.push(arr[i]);
        }
    }
    return result;
}
console.log(removeShorterStrings(
['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));
console.log(removeShorterStrings(
['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));

let arr = [1,2,3,1,4];

arr.forEach(function(num, index) {
  if (arr.indexOf(num) !== index) {
    console.log(num);
  }
});


     function removeSpaces(str) {
        let result = "";
        for(i = 0 ; i < str.length; i++){
            if(str[i] != " "){
             result+=str[i];
            }
        }
       return result; 
    }
    


console.log(removeSpaces("g eeks for ge eks"));
console.log(removeSpaces("abc d"));
