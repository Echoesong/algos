// Steps: 
// 1. Remove all non-letters, make everything lowercase
// 2. Compare if the original string minus symbols & lowercase === reverse string minus symbols & lowercase


// First go around (with internet assistance)
var isPalindrome = function(s) {
    let cache = s.split('')
    let output = []
    const check = new RegExp('[a-zA-Z0-9]');
    cache.forEach((letter, index) => {
        console.log(letter)
        if(check.test(letter)){
            output.push(letter)
        }
    });
    let forwardString = output.join('').toLowerCase()
    let reverseString = output.reverse().join('').toLowerCase()
    if(forwardString === reverseString){
        return true
    }
    return false
};

let input = "A man, a plan, a canal: Panama"

console.log(isPalindrome(input))

