from collections import Counter
import time

class Solution:
    def find_once_loop_count(self, nums: [int]) -> int:
        s = time.time()
        # [1,1,2,3,3]

        for n in nums:
            if nums.count(n) == 1:
                print(time.time() - s)
                return n


    def find_once_counter(self, nums: [int]) -> int:
        s = time.time()
        c = Counter()
        for n in nums:
            c[n] += 1
        y = [i for i in c if c[i] == 1][0]
        print(time.time() - s)
        return y

    def find_once_loop2(self, nums: [int]) -> int:
        s = time.time()
        for i in range(0, len(nums), 2):
            if i == len(nums)-1:
                print(time.time() - s)
                return nums[i]
            elif nums[i] == nums[i+1]:
                continue
            else:
                print(time.time() - s)
                return nums[i]
