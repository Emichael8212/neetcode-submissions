class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(', ']':'[', '}':'{'
        }
        if len(s) == 1:
            return False

        output = []
        for x in s:
            
            if x in dic:
                if len(output) != 0:
                    if dic[x] == output[-1]:
                        output.pop()
                    else:
                        return False
                else:
                    return False
            
            else:
                output.append(x)
        return len(output) == 0