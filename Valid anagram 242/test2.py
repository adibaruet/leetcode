class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Initialize a frequency array for 26 lowercase letters
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1  # Increment for s
            count[ord(t[i]) - ord('a')] -= 1  # Decrement for t
        
        # Check if all counts are zero
        return all(x == 0 for x in count)
