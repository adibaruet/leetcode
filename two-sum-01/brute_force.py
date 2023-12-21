from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Size of the input array
        n = len(nums)

        # Traverse the input array
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of nums[i] and nums[j] is equal to the target
                if target == nums[i] + nums[j]:
                    # Return the indices as a list
                    return [i, j]

        # No solution found, return an empty list
        return []
