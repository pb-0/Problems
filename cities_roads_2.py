class Solution:
    # O(N^2) Time | O(N) Space
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        size = len(isConnected)
        seen = [False] * size
        print('seen', seen)
        count = 0

        for node in range(size):
            print('seen[node]', seen[node])
            if not seen[node]:
                self.dfs(isConnected, seen, node)
                count += 1
                print('count ', count)

        return count

    def dfs(self, isConnected, seen, node):
        size = len(isConnected)
        print('len(isConnected)', size)
        print('node', node)

        for neighbor in range(size):
            print('neighbor ', neighbor)
            print('isConnected[node][neighbor]', isConnected[node][neighbor])
            print('seen[neighbor]', seen[neighbor])
            if isConnected[node][neighbor] == 1 and not seen[neighbor]:
                print(True)
                seen[neighbor] = True #[True, False, False] on neighbor = 0
                print(seen)
                self.dfs(isConnected, seen, neighbor)