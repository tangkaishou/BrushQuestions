


# 这道题与之前两数之和那道题的不同之处在于: 这是有序的数组
# 利用双向指针
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return [-1, -1]
        l = 0
        r = len(numbers) -1
        while (l < r):
            if numbers[l] + numbers[r] > target:
                r = r - 1
            elif numbers[l] + numbers[r] == target:
                return [l+1, r +1]
            else:
                l = l + 1
        return [-1, -1]