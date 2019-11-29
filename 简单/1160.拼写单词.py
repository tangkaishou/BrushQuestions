"""
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        import collections
        chars_dict = collections.Counter(chars)
        for word in words:
            word_dict = collections.Counter(word)
            if all([word_dict[i] <= chars_dict[i] for i in word]):
                ans += len(word)
        return ans


