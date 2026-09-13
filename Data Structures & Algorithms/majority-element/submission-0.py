class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = {}

        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1
        
        for key, value in numbers.items():
            if value > (len(nums) / 2):
                return key