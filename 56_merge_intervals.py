class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        if not intervals:
            return []
        rec_start,rec_end = intervals[0]
        for start, end in intervals[1:]:
            if start <= rec_end:
                rec_end = max(rec_end,end)
            else:
                res.append([rec_start,rec_end])
                rec_start = start
                rec_end =end
        res.append([rec_start,rec_end])

        return res

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    solution = Solution()
    res = solution.merge(intervals)
    print(res)