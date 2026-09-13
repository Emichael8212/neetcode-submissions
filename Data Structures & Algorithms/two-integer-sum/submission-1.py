class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        Input: array of integers; target integer
        Output: indices where numbers at those indices 
        sum up to the target integer

        we can use two pointers here because there is exactly
        one pair of indives to satisfy the condition

        two pointers -> left, right
        left increment condition: if we don't find any 
        complement value
        right increment condition: if we don't find any 
        complement value then move it next to left + 1
        """

        l = 0
        
        while l < len(nums):
            r = l + 1

            while r < len(nums):
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1

            l += 1