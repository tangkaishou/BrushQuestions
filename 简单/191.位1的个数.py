

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = bin(n)
        return res.count("1")
