class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumber, maxCounter = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                maxCounter += 1
            else:
                maxCounter = 0
            maxNumber = max(maxNumber, maxCounter)
        return maxNumber
        