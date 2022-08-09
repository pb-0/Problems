from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        result = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1
            print(s[right])
            print(chars)
            print("right",right)

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                print(s[left])
                print(chars)
                print("left", left)
                left += 1

            result = max(result, right - left + 1)

            right += 1
        return result

    #>>> string = "aabcddeesskjbcspdhiacn"
