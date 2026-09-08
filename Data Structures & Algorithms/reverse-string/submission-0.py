class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        s = ["n", "e", "e","t"]

        Output: ["t","e","e","n"]

        l: start of the arr 
        r: end of the arr
         update both at the same time, after swapping
        """

        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return s