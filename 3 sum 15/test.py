from typing import List  # Import List for type hinting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to use two-pointer technique

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:  
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # Fix infinite loop
                        l += 1  # Move past duplicates

        return res
