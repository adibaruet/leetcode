# Boyer-Moore Majority Voting Algo

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def majorityElement(self, nums):
        major = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                count = 1
                major = nums[i]
                continue

            if nums[i] == major:
                count += 1
            else:
                count -= 1
                
        return major
