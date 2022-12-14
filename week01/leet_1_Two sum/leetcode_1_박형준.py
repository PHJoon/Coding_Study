class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for f_idx in range(nums_len):
            for s_idx in range(f_idx + 1, nums_len):
                if nums[f_idx] + nums[s_idx] == target:
                    return [f_idx, s_idx]
