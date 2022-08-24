class Solution:
    def find_sum(self, limit: int) -> int:

        sum_limit = 0
        for n in range(limit):
            if not n % 3 or not n % 5:
                sum_limit += n

        return sum_limit