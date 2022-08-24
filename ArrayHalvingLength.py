from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        new_length = old_length = len(arr)
        i_count = Counter()

        # counter
        for i in arr:
            i_count[i] += 1

        i_s = list(i_count.keys())
        i_s.sort(key=lambda x: i_count[x])

        num = 0
        while new_length > old_length // 2:
            j = i_s.pop()
            new_length -= i_count[j]
            num += 1

        return num
