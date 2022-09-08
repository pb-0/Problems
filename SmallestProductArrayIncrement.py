import functools, heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # increment lowest number each time

        heapq.heapify(nums)

        while k:
            heapq.heappushpop(nums, nums[0] + 1)
            k -= 1

        return functools.reduce(lambda x, y: x * y % (10 ** 9 + 7), nums)