class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}

        for char in s:
            if char in char_s.keys():
                char_s[char] += 1
            else:
                char_s[char] = 1
        
        for char in t:
            if char in char_t.keys():
                char_t[char] += 1
            else:
                char_t[char] = 1

        return char_s == char_t