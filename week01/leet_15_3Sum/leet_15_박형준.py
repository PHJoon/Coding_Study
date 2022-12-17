class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)


# 훨씬 더 빠른 Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        # split nums
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)

        # if there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # if there are at least 3 zeros
        if len(z) >= 3:
            res.add((0, 0, 0))

        # for all pairs of negative check to see if their complement exists in positive
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # for all pairs positive
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
