class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        if len(nums) < 1:
            return 0
            
        while left < right:
            if nums[left] != val:
                left +=1
            else:
                if nums[right] != val:
                    nums[left], nums[right] = nums[right], nums[left]
                right -=1
        if nums[left] != val:
            return left + 1
        return left
