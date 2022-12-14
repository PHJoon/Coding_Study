class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for f_idx in range(nums_len):
            for s_idx in range(f_idx + 1, nums_len):
                if nums[f_idx] + nums[s_idx] == target:
                    return [f_idx, s_idx]

# 시간 좀 더 줄인 것


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for f_idx in range(nums_len):
            s_num = target - nums[f_idx]
            if s_num in nums[f_idx + 1:]:
                return [f_idx, f_idx + 1 + nums[f_idx + 1:].index(s_num)]


# solution 확인(시간복잡도 O(n))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
