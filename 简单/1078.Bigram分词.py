"""
输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/occurrences-after-bigram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split(" ")
        return_list = []
        for i in range(len(text_list)-2):
            if text_list[i] == first and text_list[i+1] == second:
                return_list.append(text_list[i+2])
        return return_list


""" 优秀答案
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        return [trd for fst, sed, trd in zip(text, text[1:], text[2:]) if fst == first and sed == second]

作者：wo-shi-yi-zhi
链接：https://leetcode-cn.com/problems/occurrences-after-bigram/solution/python-liang-xing-dai-ma-by-wo-shi-yi-zhi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""