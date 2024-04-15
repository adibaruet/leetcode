#time complexity O(n)
#space complexity O(1)


# Define the Solution class
class Solution:
    # Define the sortColors method
    def sortColors(self, nums):
        # Check if the length of nums is less than 2
        if len(nums) < 2:
            return
        
        # Initialize variables
        left = 0
        right = len(nums) - 1
        current = 0
        
        # Start the loop
        while current <= right:
            # Check if the current element is 0
            if nums[current] == 0:
                # Swap the current element with the element at the left pointer
                if nums[current] != nums[left]:
                    self.swap(nums, current, left)
                # Move both pointers to the right
                left += 1
                current += 1
            # Check if the current element is 1
            elif nums[current] == 1:
                # Move the current pointer to the right
                current += 1
            # If the current element is 2
            else:
                # Swap the current element with the element at the right pointer
                if nums[current] != nums[right]:
                    self.swap(nums, current, right)
                # Move the right pointer to the left
                right -= 1

    # Define the swap method
    @staticmethod
    def swap(nums, a, b):
        # Swap the elements at indices a and b in the nums list
        nums[a], nums[b] = nums[b], nums[a]

# Example usage:
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
