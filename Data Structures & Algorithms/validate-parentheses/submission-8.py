class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

        stack = []
        for i in range(len(s)):
            if s[i] in brackets:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if brackets[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
                           
        return len(stack) == 0