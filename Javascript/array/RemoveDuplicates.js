/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let u_index = 0
    for(let i = 0; i < nums.length; i++ ){
        if( nums[u_index] != nums[i]){
            u_index++;
            nums[u_index] = nums[i];
        }
    } return (u_index+1)
};