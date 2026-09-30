class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer, lenArray = 0, len(nums)

        while pointer < lenArray:
            if nums[pointer] == val:
                lenArray -= 1
                nums[pointer] = nums[lenArray]
            else:
                pointer += 1
        return lenArray

