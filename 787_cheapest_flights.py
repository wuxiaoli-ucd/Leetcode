# from collections import deque, defaultdict
#
# dist = [float('inf')] * n
# graph = defaultdict(list)
#
# for i, j, cost in flights:
#     graph[i].append((j, cost))
#
# q = deque([(src, 0)])
# step = 0
# while q and step <= k:
#
#     for _ in range(len(q)):
#         u, cost = q.popleft()
#         for v, w in graph[u]:
#             if cost + w < dist[v]:
#                 dist[v] = cost + w
#                 q.append((v, cost + w))
#     step += 1
#
# return -1 if dist[dst] == float("inf") else dist[dst]

# class Solution:
#     def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
#         memo = {}
#         possible = []
#         price = {}
#         for start, end, p in flights:
#             if start not in memo:
#                 memo[start] = []
#             memo[start].append(end)
#             price[(start, end)] = p
#
#         def dfs(start, path):
#             if len(path) > (k + 2):
#                 return
#             if start == dst:
#                 possible.append(path[:])
#                 return
#             # 这里要注意这里是很可能为空的。然后还要注意的是，这个dfs很可能会无限循环，因为有环
#             for end in memo.get(start, []):
#                 path.append(end)
#                 dfs(end, path)
#                 path.pop()
#
#         dfs(src, [src])
#         min_price = []
#         for route in possible:
#             if len(route) > k + 2:
#                 continue
#             p = 0
#             for i in range(len(route) - 1):
#                 p += price[(route[i], route[i + 1])]
#             min_price.append(p)
#
#         if not min_price:
#             return -1
#         return min(min_price)

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]
            for start, end, price in flights:
                if prices[start] == float("inf"):
                    continue
                temp[end] = min(temp[end], prices[start] + price)
            prices = temp[:]

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]





