# Solution 1: BFS
from collections import defaultdict
from collections import deque


class Solution_bfs:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        q = deque([0])
        visited = {0}
        res = 0

        while q:
            city = q.popleft()

            for neighbor, cost in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res += cost
                    q.append(neighbor)

        return res

class Solution_dfs:
    def minReorder_dfs(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = {0}
        res = [0]
        self.dfs(0, graph, visited, res)

        return res[0]

    def dfs(self, city: int, graph: dict, visited: set, res: list[int]) -> None:
        visited.add(city)

        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                res[0] += cost
                self.dfs(neighbor, graph, visited, res)
class Solution:
    def minReorder_dfsc(self, n: int, connections: list[list[int]]) -> int:
        self.res = 0
        roads = set()
        graph = defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            print(roads)
            graph[v].append(u)
            print("added to", graph)
            graph[u].append(v)
            print("added from", graph)

        def dfs(u, parent):
            print("u, parent:",u,parent)
            self.res += (parent, u) in roads # increment if (parent, u) in roads
            print("res ",self.res)
            for v in graph[u]: #for roads-to from city u
                if v == parent: #if roads_to is in parent, skip increment
                    continue
                dfs(v, u) #not in parent, run dfs again
        dfs(0, -1)
        return self.res


def minReorder(self, n: int, connections: list[list[int]]) -> int:
    graph = defaultdict(list)
    roads = set()

    for o, d in connections:
        graph[o].append(d)
        graph[d].append(o)
        roads.add((o, d))

    def dfs(node, parent):

        ans = 0
        if (parent, node) in roads:
            ans += 1

        for child in graph[node]:
            if child != parent:
                ans += dfs(child, node)
        return ans

    return dfs(0, -1)


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        d = defaultdict(dict)
        for a, b in connections:
            d[a][b] = 1
            d[b][a] = 0

        seen = set()

        def dfs(a):
            seen.add(a)
            return sum(d[a][b] + dfs(b) for b in d[a] if b not in seen)

        return dfs(0)