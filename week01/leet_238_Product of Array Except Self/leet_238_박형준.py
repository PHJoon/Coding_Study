class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def check_zero_arr(nums):
            cnt = 0
            for n in nums:
                if n == 0:
                    cnt += 1
            if cnt >= 2:
                return 1
            return 0

        if check_zero_arr(nums) == 1:
            return [0] * len(nums)

        whole_p = 1
        for n in nums:
            if n != 0:
                whole_p *= n
        res = [whole_p] * len(nums)
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res[i] = 0
        else:
            for i in range(len(nums)):
                res[i] //= nums[i]
        return res
