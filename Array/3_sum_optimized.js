function three_sum(nums){

    let res = [];
    nums.sort((a,b)=> a - b); // JS sorting based on hybrid sorting

    for(let i=0; i<nums.length - 2; i++){
        // if(i >0 && nums[i] == nums[i-1]){continue};

        let left = i+1;
        let right = nums.length - 1;
        while(left<right){
            let triplet =  nums[i] +nums[left] +nums[right];
            // let exists = res.some(t => t[0]=== triple[0] && t[1]===triplet[1] && t[2]=== triplet[2]);
            let exists = res.some(t => t[0]===nums[i] && t[1] === nums[left] && t[2] === nums[right]);
            // console.log(exists)
            
            if(triplet === 0 && !exists){
                res.push([nums[i], nums[left], nums[right]]);
                left ++ ;
                right --;

            }
            else if(triplet > 0){
                right --;
            }
            else{
                left ++;
            }

        }
    }

    return res;


}

const nums = [1,0,-1,2,0,-2,5,-5,0,-3,1,2];
console.log(three_sum(nums))
