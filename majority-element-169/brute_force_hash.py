#Time Complexity: O(n)
#Space Complexity: O(u)--close to 1
class Solution:
    def majorityElement(self, nums):
        num_count = {}  # Hashmap to store the count of each element

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # Find the element with the maximum count in the hashmap
        majority_element = max(num_count, key=num_count.get)

        return majority_element
