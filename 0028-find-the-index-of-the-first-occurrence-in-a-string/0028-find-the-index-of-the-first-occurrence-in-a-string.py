class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: If needle is longer than haystack, it can't be a part of it
        if len(needle) > len(haystack):
            return -1
            
        # We only need to loop up to the point where needle can physically fit
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring matches the needle
            if haystack[i:i + len(needle)] == needle:
                return i
                
        return -1