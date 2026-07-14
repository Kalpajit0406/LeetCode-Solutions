class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by default whitespace, which handles multiple spaces,
        # then reverse the list of words and join with a single space.
        return " ".join(s.split()[::-1])