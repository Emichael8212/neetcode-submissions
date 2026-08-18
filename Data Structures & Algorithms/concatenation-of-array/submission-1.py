class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_arr_len = 2 * n
        ans = [0] * new_arr_len

        p_nums = 0
        for i in range(len(ans)):
            ans[i] = nums[p_nums]

            if p_nums + 1 == len(nums):
                p_nums = 0
            else:
                p_nums += 1
        return ans