class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        observed_vals = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in observed_vals:
                return [observed_vals[diff], i]
            observed_vals[num] = i