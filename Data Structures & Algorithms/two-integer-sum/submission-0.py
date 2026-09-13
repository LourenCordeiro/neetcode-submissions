class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valor = {}

        for i, num in enumerate(nums):
            resolution = target - num
            if resolution in valor:
                j = valor[resolution]
                return [j, i]
            valor[num] = i

        