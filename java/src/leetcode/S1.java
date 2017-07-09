package leetcode;

import java.util.HashMap;

public class S1 {

    public class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                Integer pair = map.get(target - nums[i]);
                if (pair != null) {
                    return new int[]{pair, i};
                }
                map.put(nums[i], i);
            }
            return null;
        }
    }
}
