class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += s_nums[i]
        return res
