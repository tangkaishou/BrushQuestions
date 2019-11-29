"""
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")