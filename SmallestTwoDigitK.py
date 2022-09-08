import collections
class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        mi = min(digit1, digit2)
        ma = max(digit1, digit2)
        qu = collections.deque([mi, ma] if mi != ma else [mi])
        while qu:
            cur = qu.popleft()
            if cur == 0 or cur > 2 ** 31 - 1:
                continue
            if cur > k and cur % k == 0:
                return cur
            qu.append(cur * 10 + mi)
            if mi != ma:
                qu.append(cur * 10 + ma)
        return -1