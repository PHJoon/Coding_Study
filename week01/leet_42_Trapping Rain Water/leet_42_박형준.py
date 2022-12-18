class Solution:
    def trap(self, height: List[int]) -> int:
        def asc_end(height, i):
            for idx in range(i, len(height)):
                if idx == len(height) - 1:
                    break
                if height[idx] > height[idx + 1]:
                    break
            return idx

        def desc_end(height, i):
            for idx in range(i, len(height)):
                if idx == len(height) - 1:
                    break
                if height[idx] < height[idx + 1]:
                    break
            return idx

        def hole_size(hole):
            if hole[0] > hole[-1]:
                hole[0] = hole[-1]
            elif hole[0] < hole[-1]:
                hole[-1] = hole[0]
            cnt = 0
            for i in hole:
                if hole[0] - i > 0:
                    cnt += hole[0] - i
            return cnt

        def check_big_hole(height, hole):
            tmp_1 = sorted(height, reverse=True)
            max_a = tmp_1[0]
            max_b = tmp_1[1]
            if max_a == max_b:
                tmp_2 = [i for i, x in enumerate(height) if x == max_a]
                a_idx = tmp_2[0]
                b_idx = tmp_2[-1]
            else:
                a_idx = height.index(max_a)
                b_idx = height.index(max_b)
            start = min(a_idx, b_idx)
            end = max(a_idx, b_idx)
            if abs(start - end) == 1:
                return height
            hole.append(height[start:end + 1])
            height = height[0:start] + height[end + 1:]

            return height

        hole = []
        size = 0
        if len(height) <= 2:
            return size
        height = check_big_hole(height, hole)
        if len(height) != 0:
            ptr = asc_end(height, 0)
            while ptr != len(height) - 1:
                middle = desc_end(height, ptr)
                if middle == len(height) - 1:
                    break
                end = asc_end(height, middle)
                hole.append(height[ptr:end + 1])
                ptr = end
        for h in hole:
            size += hole_size(h)
        return size
