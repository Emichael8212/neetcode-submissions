class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        indicator = 0
        changer = indicator+1

        while changer < len(arr):
            arr[indicator] = max(arr[changer:])
            indicator += 1
            changer += 1
        arr[-1] = -1
        return arr