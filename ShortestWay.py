from collections import defaultdict
from bisect import bisect_left

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_index = defaultdict(list)
        for i, ch in enumerate(source):
            inverted_index[ch].append(i)

        loop_cnt = 1
        i = -1
        for ch in target:
            print("ch",ch)
            if ch not in inverted_index:
                return -1
            offset_list_for_ch = inverted_index[ch]
            print("offset_list_for_ch", offset_list_for_ch)
            j = bisect_left(offset_list_for_ch, i)
            print("i", i)
            print("j", j)
            if j == len(offset_list_for_ch):
                loop_cnt += 1
                i = offset_list_for_ch[0] + 1
            else:
                i = offset_list_for_ch[j] + 1 #i +2 [a--bc] [abc--]
            print("i", i)
            print("loop_cnt", loop_cnt)

        return loop_cnt