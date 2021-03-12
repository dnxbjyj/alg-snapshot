# version: V2
# AC@5076ms, 5%, 36%, O(n^2), O(1)
# 相比于上一个版本（V1）AC原因：正确处理了对边界柱子的可贡献容量
from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        # - 边界判断
        if not height or len(height) == 0:
            return 0

        # - 暴力解法O(n^2)
        size = len(height)
        # [核心思想] 局部贡献思想：height[i]柱子可局部贡献的容量为：res = min(max(height[0...i-1]), max(height[i+1...size-1])) - height[i]，注意：如果左、右最大高度都小于或等于当前高度，则当前柱子是无法贡献容量的。特别的，当i=0时认为左边的height[-1]为0；当i=size-1时认为右边的height[size]为0。所有柱子可容纳的总容量为：sum(res0, res1,..., resN), 其中N = size - 1

        # 总容量
        res = 0
        for i in range(size):
            # height[0...i-1]的最大值
            left_max = 0
            # height[i+1...size-1]的最大值
            right_max = 0
            if i == 0:
                # 左边最大值（认为是heigth[-1]）为0，所以当前柱子可贡献的容量为0
                continue
            elif i == size - 1:
                # 右边最大值（认为是heigth[size]）为0，所以当前柱子可贡献的容量为0
                continue
            else:
                for j in range(0, i):
                    if height[j] > left_max:
                        left_max = height[j]
                for j in range(i+1, size):
                    if height[j] > right_max:
                        right_max = height[j]
                lower_height = min(left_max, right_max)
                # 左、右最大高度至少有一个大于当前高度，才能让当前柱子贡献容量
                if lower_height > height[i]:
                    res = res + (lower_height - height[i])
        return res
                
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
