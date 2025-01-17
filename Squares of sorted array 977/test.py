from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squared_nums = [x ** 2 for x in nums]

        sorted_squares = sorted(squared_nums)
        
        return sorted_squares  

solution = Solution()
nums = [-4, -1, 0, 3, 10]
print(solution.sortedSquares(nums))
