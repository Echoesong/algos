function productExceptSelf(nums) {
    let length = nums.length;
    let answer = Array(length).fill(1);

    let left = 1;
    for (let i = 0; i < length; i++) {
        answer[i] *= left;
        left *= nums[i];
    }

    let right = 1;
    for (let i = length - 1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }

    return answer;
}
let numbers = [-1,1,0,-3,3]
console.log(productExceptSelf(numbers)) 