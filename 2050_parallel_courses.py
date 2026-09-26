from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        # prev-->next
        graph = {}
        # next --> number of prev
        check = {}
        tovisit = deque()
        finish = {}
        # look relations,save check[coures] = number of prev.
        # save relations into graph graph[prev]=[next...]

        for course in range(1, n + 1):
            graph[course] = []
            check[course] = 0
            finish[course] = time[course - 1]

        for prev, next in relations:
            graph[prev].append(next)
            check[next] += 1

        for i in check:
            if check[i] == 0:
                tovisit.append(i)

        # BFs
        while len(tovisit) > 0:
            for i in range(len(tovisit)):
                target = tovisit.popleft()

                for j in graph[target]:
                    finish[j] = max(finish[j], time[j - 1] + finish[target])
                    check[j] -= 1
                    if check[j] == 0:
                        tovisit.append(j)

        min_month = 0
        for course in finish:
            if finish[course] > min_month:
                min_month = finish[course]
        return min_month

    def minTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = {}
        memo = {}

        for course in range(1, n + 1):
            graph[course] = []

        for prev, nxt in relations:
            graph[nxt].append(prev)

        def dfs(course):
            if course in memo:
                return memo[course]
            max_prev = 0
            for prev in graph[course]:
                max_prev = max(max_prev, dfs(prev))
            memo[course] = max_prev + time[course-1]
            return memo[course]

        max_month = 0
        for i in range(1,n+1):
            max_month = max(max_month, dfs(i))
        return max_month





