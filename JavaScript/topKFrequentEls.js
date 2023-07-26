// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// notes: 
/*
Will almost certainly iterate over nums, splitting them into separate structures (all 1s, all 2s, etc)
Compare length, use length to return a number for its ranking (so longest would be 1, 2nd longest would be 2, so on)
Return each structure that is <= k
possibly use below Map syntax for sorting: 

if(map1.has(sorted)){map1.get(sorted).push(string)}
       else{map1.set(sorted, [string])}

*/

var topKFrequent = function(nums, k) {
    let map1 = new Map()
    let cache = []
    let output = []
    nums.forEach(num => {
        if(map1.has(num)){
            map1.get(num).push(num)
        } else{
            map1.set(num, [num])
        }
    });
    let mapEntries = [...map1.entries()]
    mapEntries.sort((a, b) => b[1].length - a[1].length)
    let sortedMap = new Map(mapEntries)
    while(k>0){
        let firstKey = sortedMap.keys().next().value
        output.push(firstKey)
        sortedMap.delete(firstKey)
        k--
    }
    return output
};

let numbers = [1,1,1,2,2,3] 
let kIn = 2
Output: [1,2]

console.log(topKFrequent(numbers, kIn))


// map1.forEach(val => {
//     let length = val.length
//     cache.push(length)
//     val.push(length)
// })
// cache.sort(function(a, b){return b - a})
// while(k > 0){
//     let frequency = cache.splice(0,1)
//     output.push()
// }