class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # Check if this subproblem has already been solved
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Base Cases
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        # If character counts don't match, s2 cannot be a scramble of s1
        if sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False
            
        n = len(s1)
        
        # Try splitting the string at every possible pivot point
        for i in range(1, n):
            # Case 1: Substrings are NOT swapped
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                self.memo[(s1, s2)] = True
                return True
                
            # Case 2: Substrings WERE swapped
            if (self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i])):
                self.memo[(s1, s2)] = True
                return True
                
        self.memo[(s1, s2)] = False
        return False