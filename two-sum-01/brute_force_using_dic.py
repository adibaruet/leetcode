from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Dictionary to store the complement of each number along with its index

        # Traverse the input array
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_dict:
                # Return the indices as a list
                return [num_dict[complement], i]

            # Store the current number and its index in the dictionary
            num_dict[num] = i

        # No solution found, return an empty list
        return []
