from typing import List
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        count = {}
        res = [0] * 5
        for x, y in coordinates:
            ref = [(0,0),(0,-1),(-1,0),(-1,-1)]
            for dr,dc in ref:
                nr = x + dr
                nc = y + dc
                if nr >=0 and nc >=0 and nr < m-1 and nc < n-1:
                    count[(nr,nc)] = count.get((nr,nc),0) + 1

        total = (m-1) *(n-1)
        count_0 = total - len(count)

        res[0] = count_0
        for i in count:
            res[count[i]] += 1
        return res

# 主要是注意标签命名这块。。。