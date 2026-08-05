import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        postfix = nums.copy()
        for i in range(len(nums)-1):
            prefix[i+1] *= prefix[i]
        
        for j in range(len(nums)-1, 0, -1):
            postfix[j-1] *= postfix[j]
        
        for k in range(len(nums)):
            if k == 0: nums[k] = postfix[k+1]
            elif k == len(nums)-1: nums[k] = prefix[k-1]
            else:
                nums[k] = prefix[k-1]*postfix[k+1]
        
        return nums


        