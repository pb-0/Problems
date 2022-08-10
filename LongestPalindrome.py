from collections import deque


class Solution:

    def longestPalindrome(self, s: str) -> str:
        ss = []
        gs = 0
        for n in range(len(s)):  # iterate string
            ps = [s[n]]
            for i in range(1, len(s) - n):  # iterate all substrings from
                if i == 1:
                    ps.append(s[n + i])
                elif i > 1 and s[n + i] == s[n]:
                    ps.append(s[n + i])
                else:
                    break

            if len(ps) == 1:
                ss.append(ps)
            elif len(ps) == 2 and ps[0] == ps[1]:
                ss.append(ps)
            elif len(ps) > 2:  # append all valid small palindromes
                ss.append(ps)

        ss = list(map("".join, ss))

        q = list(map(deque, ss))
        print(s)
        print(q)
        print(ss)
        for l in range(len(q)):
            # print(l)                    10     8.             1
            if s.find(ss[l]) > 0 and len(s) - len(ss[l]) - s.find(ss[l]) > 0:  # doesn't append for l = 0
                # print(True)
                if s[s.find(ss[l]) - 1] == s[s.find(ss[l]) + len(ss[l])]:
                    # print(q[l])
                    # print(len(q))
                    # print(l)
                    q[l].appendleft(s[s.find(ss[l]) - 1])
                    q[l].append(s[s.find(ss[l]) + len(ss[l])])

        print(q)
        q.sort(key=lambda x: len(x), reverse=True)
        if len(s) == 1:
            res = s
        else:
            res = "".join(list(q[0]))

        return res