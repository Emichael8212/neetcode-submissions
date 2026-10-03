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
                if output:
                    if dic[char] == output[-1]:
                        output.pop()
                    else:
                        return False
                else:
                    return False
            
            else:
                output.append(char)
        return len(output) == 0