class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(target - nums[i]) != i:
                return [nums.index(target - nums[i]), i]