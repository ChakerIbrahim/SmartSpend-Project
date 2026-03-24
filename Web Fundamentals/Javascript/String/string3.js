//isValidParentheses// ()true ))(( false
function isValidParentheses(str) {
    let count = 0;
    for (i = 0; i < str.length; i++) {
        if (str[i] === '(') {
            count++;
        }
        else if (str[i] === ')') {
            count--;

            if (count < 0) {
                return false;
            }
        }
    }
    return count === 0;
}


console.log(isValidParentheses("Y(3(p)p(3)r)s"));
console.log(isValidParentheses("N(0(p)3"));
console.log(isValidParentheses("N(0)t )0(k"));    

//(){}//
function isValid(str) {
    let stack = [];
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        }
        else if (char === ')' || char === '}' || char === ']') {
            if (stack.length === 0) {
                return false;
            }
            let last = stack.pop();
            if (
                (char === ')' && last !== '(') ||
                (char === '}' && last !== '{') ||
                (char === ']' && last !== '[')
            ) {
                return false;
            }
        }
    }
    return stack.length === 0;
}
console.log(isValid("()"));        
console.log(isValid("([])"));     
console.log(isValid("(]"));        
console.log(isValid("([)]"));      
console.log(isValid("{[]}"));    

//Palindrome//
function isPalindrome(str){
    for(i = 0;i < str.length / 2 ;i++){
        if(str[i] !== str[str.length - 1 - i]){
            return false;
        }
    }
    return true;
}
console.log(isPalindrome("ablE was I ere I saw Elba"));
//
function isPalindrome(str) {
    return str === str.split('').reverse().join('');
}
function longestPalindromeSubstring(str) {
    let longest = "";

    for (let x = 0; x < str.length; x++) {
        for (let j = x + 1; j <= str.length; j++) {
            let sub = str.slice(x, j);

            if (isPalindrome(sub) && sub.length > longest.length) {
                longest = sub;
            }
        }
    }

    return longest;
}
console.log(longestPalindromeSubstring("Hot puree eruption!"));