from collections import Counter
class Solution:
    def LongestSubstring(self, s : str) -> [int, str]:
        c_count = Counter()
        'aaabbcada'
        for n in range(len(s)): # iterate string
            c_count[n] = 1
            # n = 4
            for i in range(1, len(s) - n): # iterate next sequences
                # i = 1
                if s[n] == s[n + i]:
                    break
                elif s[n] != s[n + i]:
                    if s[n + i] not in s[n: n + i]:
                        c_count[n] += 1
                    else:
                        break

        start = max(c_count, key=c_count.get)
        length = c_count[start]

        substring = s[start : start + length]
        longest = (length, substring)

        return longest

    def LongestSubstring_nc(self, s : str) -> [int, str]:
        'aaabbcada'
        longest = 0
        for n in range(len(s)): # iterate string
            count = 1
            # n = 4
            for i in range(1, len(s) - n): # iterate next sequences
                # i = 1
                if s[n] == s[n + i]:
                    break
                elif s[n] != s[n + i]:
                    if s[n + i] not in s[n: n + i]:
                        count += 1
                    else:
                        break
            longest = max(longest, count)

        return longest