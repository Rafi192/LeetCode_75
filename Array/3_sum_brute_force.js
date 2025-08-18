var threeSum = function(nums) {
    // let res = [];
    let res = new Set();
    nums.sort((a, b) => a - b); // sort first to help avoid duplicates

    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length ; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (nums[i] + nums[j] + nums[k] === 0) {
                    let triplet = [nums[i], nums[j], nums[k]];
                    res.add((JSON.stringify(triplet)))

                    // check if this triplet is already in res
                    // let exists = res.some(t => t[0] === triplet[0] && t[1] === triplet[1] && t[2] === triplet[2]);
                    // if (!exists) {
                    //     res.push(triplet);
                    // }
                }
            }
        }
    }

    return Array.from(res).map(JSON.parse)
};


const nums = [1,0,-1,2,0,-2,5,-5,0,-3,1,2];
console.log(threeSum(nums))
