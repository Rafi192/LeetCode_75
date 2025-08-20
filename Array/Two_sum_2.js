var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    // for(const num of numbers){
        while(left < right){
        // let two_sum = numbers[left] + numbers[right];

        if( numbers[left] + numbers[right] === target){
            return [left+1 , right+1];
        }
        else if(numbers[left] + numbers[right] > target  ){
            right --;
        }
        else if( numbers[left] + numbers[right]< target  ){
            left++;
        }
    }

        // }
    // return []
    
};