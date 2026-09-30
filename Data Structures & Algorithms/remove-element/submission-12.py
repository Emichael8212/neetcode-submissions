class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer_pointer = 0
        for reader_pointer in range(len(nums)):
            if nums[reader_pointer] != val:
                nums[writer_pointer] = nums[reader_pointer]
                writer_pointer += 1
        return writer_pointer

