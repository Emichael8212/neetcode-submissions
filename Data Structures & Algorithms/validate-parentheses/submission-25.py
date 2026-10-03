class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(', ']':'[', '}':'{'
        }
        if len(s) == 1:
            return False

        output = []
        for char in s:
            if char in dic:
                if not output or dic[char] != output[-1]:
                    return False
                output.pop()
            else:
                output.append(char)
        return len(output) == 0