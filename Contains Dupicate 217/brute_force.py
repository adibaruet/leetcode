# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    print("True")
                    return True
        print("False")
        return False
