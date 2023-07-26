var groupAnagrams = function(strings) {
    const map1 = new Map()
    strings.forEach(string => {
       let sorted = string.split('').sort().join('')
       if(map1.has(sorted)){map1.get(sorted).push(string)}
       else{map1.set(sorted, [string])}
    });
    let output = [...map1.values()]
    return output
};

let strings = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

console.log(groupAnagrams(strings))