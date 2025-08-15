// This problem can be solved using both Set and Map 
// THe solution given for all the methods

var twoSum = function(nums, target) {

    let seen_set = new Set();
    // let seen_map = new Map();
    for (let i = 0; i <nums.length; i++){
        const y = (target - nums[i]);
        if(seen_set.has(y)){
            const index_y = nums.indexOf(y);
            // const index_y = seen_map.get(y)
            return [index_y, i];
        }

        seen_set.add(nums[i]) ;
        // seen_map.set((nums[i]), i);
    }

    
};