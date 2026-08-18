class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        for i in range(len(arr)-1, -1, -1):
            original = arr[i]
            arr[i] = max_num

            if original > max_num:
                max_num = original
        return arr