class Solution:
    def wordPattern(self, pattern: str, lstr: str) -> bool:
        lstr = lstr.split(" ")
        return list(map(pattern.index, pattern)) == list(map(lstr.index, lstr))
        # return [*map(pattern.index, pattern)] == [*map(lstr.index, lstr)]
