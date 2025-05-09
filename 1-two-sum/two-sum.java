import java.util.Hashtable;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable < Integer,Integer> numbersFound = new Hashtable<>();
        for (int i = 0; i < nums.length; i++ ){
            if (numbersFound.containsKey(target - nums[i])){
                return new int [] { numbersFound.get (target - nums[i]),i};
            }
            numbersFound.put(nums[i],i);

        }
        return null;
    }
}