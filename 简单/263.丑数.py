class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while True:
            last = num
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            if num == 1:
                return True
            if last == num:
                return False  # 一轮下来都不满足的话、那就是不合适了。
