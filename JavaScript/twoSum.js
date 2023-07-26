var twoSum = function(numbers, target) {
    let output = []
    numbers.forEach((num, idx) => {
        for(let i = idx + 1; i < numbers.length; i++) {
            if(num + numbers[i] == target) {
                output = [idx, i]
                break
            }
        }
    })
    return output
};

let numbers = [2,7,11,15] 
let target = 9
Output: [0,1]

console.log(twoSum(numbers, target))