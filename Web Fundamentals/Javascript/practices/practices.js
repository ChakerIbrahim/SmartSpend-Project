
//Reverse a String//

function reverseString(string) {
    var newString = "";
    for (var i = string.length - 1; i >= 0; i--) {
        newString += string[i];
    }
    return newString;
}

console.log(reverseString("Hello"))

//Count Vowels//

function countVowels(str) {
    var vowels = ["a", "e", "i", "o", "u"];
    var count = 0;

    for (var i = 0; i < str.length; i++) {
        var letter = str[i].toLowerCase();

        if (vowels.includes(letter)) {
            count++;
        }
    }

    return count;
}
console.log(countVowels("hello"));

//Check Palindrome//

function isPalindrome(str) {
    var reversed = "";

    for (var i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }

    return str === reversed;
}
console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));

//Longest Word in a Sentence//
function longestWord(sentence) {
    var words = sentence.split(" ");
    var longest = "";

    for (var i = 0; i < words.length; i++) {
        if (words[i].length > longest.length) {
            longest = words[i];
        }
    }

    return longest;
}
console.log(longestWord(["jalil","lina","rayn","hi"]))
//////////////////////////////////////
//Convert a Letter Grade to Feedback//

function marks(grade) {
    var result = "";

    switch (grade) {
        case "A":
            result = "Excellent";
            break;
        case "B":
            result = "Good job";
            break;
        case "C":
            result = "You passed";
            break;
        case "D":
            result = "Need improvement";
            break;
        case "F":
            result = "Failed";
            break;
        default:
            result = "Invalid grade";
    }

    return result;
}

console.log(marks("Z"));
////////////////////////////////////////
////Count Character Types in a String //
function countCharacters(str) {
    var result = {
        vowels: 0,
        digits: 0,
        spaces: 0,
        others: 0
    };

    for (var i = 0; i < str.length; i++) {
        var char = str[i].toLowerCase();

        switch (true) {

            case "aeiou".includes(char):
                result.vowels++;
                break;

            case char >= "0" && char <= "9":
                result.digits++;
                break;

            case char === " ":
                result.spaces++;
                break;

            default:
                result.others++;
        }
    }

    return result;
}

console.log(countCharacters("Hi 123!"));