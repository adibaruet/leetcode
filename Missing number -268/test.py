from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i  # Missing number found
        
        return len(nums)
