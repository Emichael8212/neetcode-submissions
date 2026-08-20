class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '{': '}', '[': ']', '(': ')'
        }

        stack = []
        for char in s:
            if char in dic:
                stack.append(char)
            else:
                if not stack:
                    return False
                if dic[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    