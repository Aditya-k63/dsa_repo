class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(i * (26 - ord(ch) + 97) for i, ch in enumerate(s, 1))