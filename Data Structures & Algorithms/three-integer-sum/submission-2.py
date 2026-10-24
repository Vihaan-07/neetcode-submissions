class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -val:
                    output.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                
                if nums[l] + nums[r] > -val:
                    r -=1
                else:
                    l += 1
        return output

        