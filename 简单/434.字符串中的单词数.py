

class Solution:
    def countSegments(self, s: str) -> int:
        slist = s.split(' ')
        count = 0
        for i in slist:
            if len(i):
                count += 1
        return count