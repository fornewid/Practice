class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) is None:
                dict[target - nums[i]] = i
            else:
                return [dict[nums[i]], i]