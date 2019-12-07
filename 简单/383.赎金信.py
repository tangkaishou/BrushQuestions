

# 包含于被包含的关系
# 并集 == 大的
# 交集 == 小的
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        return (ransomCounter | magazineCounter ) == magazineCounter