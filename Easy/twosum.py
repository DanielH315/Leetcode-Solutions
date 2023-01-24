class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        hashmap = {}
        final = []

        complement = 0 

        for i in range(len(nums)):  
            complement = target - nums[i] #c = 9 - 7 = 2

            if complement in hashmap:
                final.append(hashmap[complement])
                final.append(i)
                return final
            hashmap[nums[i]] = i #{2:0}
