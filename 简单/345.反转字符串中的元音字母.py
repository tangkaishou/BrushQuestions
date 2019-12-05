
# 双指针做法
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        p1, p2 = 0, len(arr) - 1
        while p1 < p2:
            while arr[p1] not in vowel and p1 < p2:
                p1 += 1
            while arr[p2] not in vowel and p1 < p2:
                p2 -= 1
            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1
        return ''.join(arr)

# 作者：larger5
# 链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string/solution/shuang-zhi-zhen-python-jie-fa-by-larger5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。