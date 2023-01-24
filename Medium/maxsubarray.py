#https://leetcode.com/problems/maximum-subarray/description/

import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total_max = nums[0]
        curr_max = nums[0]

        for x in range(1, len(nums)):
            
            if nums[x] < (curr_max + nums[x]):
                curr_max = curr_max + nums[x]
            else:
                curr_max = nums[x]
            
            if curr_max > total_max:
                total_max = curr_max
            
        return total_max

            

