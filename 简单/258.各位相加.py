class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            n = sum([int(i) for i in str(num)])
            return self.addDigits(n)
