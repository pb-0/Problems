class Solution:
    def convertToBase7(self, num: int) -> str:

        b = ""

        if num == 0:
            return "0"

        neg_flag = False
        if num < 0:
            neg_flag = True
            num = -num

        while num:
            b += str(num % 7)
            num //= 7

        # if abs(num)/7 == 1:
        #     b = str(num//7) + "0"

        # 100 / 7
        #     14 -> 2 remainder
        #     14 /7 = 2 -> 0 remainder
        #     2 remainder

        return ('-' if neg_flag else '') + b[::-1]