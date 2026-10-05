class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(', ']':'[', '}':'{'
        }
        

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