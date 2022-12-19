# 타임아웃
class Solution:
    def trap(self, height: List[int]) -> int:

        def check_floor(height, len_h):
            floor_x = [0] * len_h
            for i in range(len_h):
                if height[i] > 0:
                    floor_x[i] = 1
                    height[i] -= 1
            return floor_x

        def get_hole_size(floor):
            i = 0
            while floor[i] == 0 and i < len(floor):
                i += 1
            j = len(floor) - 1
            while floor[j] == 0 and j > -1:
                j -= 1
            if i >= j:
                return (0)
            size = floor[i:j + 1].count(0)
            return size

        len_h = len(height)
        max_h = max(height)
        size = 0
        for i in range(1, max_h + 1):
            floor = check_floor(height, len_h)
            size += get_hole_size(floor)
        return size
