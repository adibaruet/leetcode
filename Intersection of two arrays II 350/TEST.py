from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each number in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection
        intersection = []
        for num in count1:
            if num in count2:
                # Add the minimum of counts from both arrays
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection
