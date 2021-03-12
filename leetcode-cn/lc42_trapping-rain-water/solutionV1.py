# version: V1
# NC
# NC原因：当i==0时，无论右边最高柱子有多高，当前柱子都是无法贡献容量的（因为认为height[-1]为0而非无穷大）；当i==size-1时同理
from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        # - 边界判断
        if not height or len(height) == 0:
            return 0

        # - 暴力解法O(n^2)
        size = len(height)
        # [核心思想] 局部贡献思想：height[i]柱子可局部贡献的容量为：res = min(max(height[0...i-1]), max(height[i+1...size-1])) - height[i]，注意：如果左、右最大高度都小于或等于当前高度，则当前柱子是无法贡献容量的。所有柱子可容纳的总容量为：sum(res0, res1,..., resN), 其中N = size - 1

        # 总容量
        res = 0
        for i in range(size):
            # height[0...i-1]的最大值
            left_max = 0
            # height[i+1...size-1]的最大值
            right_max = 0
            if i == 0:
                for j in range(i+1, size):
                    if height[j] > right_max:
                        right_max = height[j]
                # 右边最大高度要大于当前高度，才能让当前柱子贡献容量
                if right_max > height[i]:
                    res = res + (right_max - height[i])
            elif i == size - 1:
                for j in range(i):
                    if height[j] > left_max:
                        left_max = height[j]
                # 左边最大高度要大于当前高度，才能让当前柱子贡献容量
                if left_max > height[i]:
                    res = res + (left_max - height[i])
            else:
                for j in range(0, i):
                    if height[j] > left_max:
                        left_max = height[j]
                for j in range(i+1, size):
                    if height[j] > right_max:
                        right_max = height[j]
                lower_height = min(left_max, right_max) - height[i]
                # 左、右最大高度至少有一个大于当前高度，才能让当前柱子贡献容量
                if lower_height > height[i]:
                    res = res + (lower_height - height[i])
        return res
                
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
