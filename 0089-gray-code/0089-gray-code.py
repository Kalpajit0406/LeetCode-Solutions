class Solution:
    def grayCode(self, n: int) -> list[int]:
        # There are 2^n elements in an n-bit Gray code sequence
        num_elements = 1 << n
        
        # Generate the sequence using the formula: i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(num_elements)]