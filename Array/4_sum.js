// /**
//  * @param {number[]} nums
//  * @param {number} target
//  * @return {number[][]}
//  */
var fourSum = function(nums, target) {
    let res = [];
    nums.sort((a,b) => a-b); // sort numerically

    for (let i = 0; i < nums.length - 3; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue; // skip duplicate

        for (let j = i+1; j < nums.length - 2; j++) {
            if (j > i+1 && nums[j] === nums[j-1]) continue; // skip duplicate

            let left = j+1;
            let right = nums.length-1;

            while (left < right) {
                let sum = nums[i] + nums[j] + nums[left] + nums[right];
                if (sum === target) {
                    res.push([nums[i], nums[j], nums[left], nums[right]]);

                    // skip duplicates
                    while (left < right && nums[left] === nums[left+1]) left++;
                    while (left < right && nums[right] === nums[right-1]) right--;

                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }
    return res;
};
