class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [(0, 0, "")] 

        while stack:
            left, right, s = stack.pop()

            if left == n and right == n:
                result.append(s)
                continue

            if left < n:
                stack.append((left + 1, right, s + "("))
            if right < left:
                stack.append((left, right + 1, s + ")"))

        return result   