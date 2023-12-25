#Time Complexity: O(n log n)
#Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
