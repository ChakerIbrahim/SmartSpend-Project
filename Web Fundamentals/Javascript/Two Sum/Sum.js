let arr = [2,7,11,15,4,5];
let target = 9;
for(i=0;i<arr.length;i++){
    for(j=i+1;j<arr.length;j++){
        if(arr[i]+arr[j]== target){
             console.log(`Pair found: ${arr[i]} + ${arr[j]} = ${target}`);
             break;
       }
    }
 if (arr[i] + arr[j] == target) {
        break;
 }
}
/////////////////////////////////////////////////////////////////////////////////
function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
}
console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([3,2,4],6));
console.log(twoSum([3,3],6));