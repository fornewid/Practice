package leetcode

class Solution {

    companion object {

        fun twoSum(nums: IntArray, target: Int): IntArray? {
            val map = mutableMapOf<Int,Int>()
            for (i in nums.indices) {
                val pair = map[target - nums[i]]
                if (pair == null) {
                    map[nums[i]] = i
                } else {
                    return intArrayOf(pair, i)
                }
            }
            return null
        }
    }
}
