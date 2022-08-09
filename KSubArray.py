class Solution:
    def FindKDistinctSubArray(self, nums: list[int], k: int) -> int:
        ## in: nums = [1,2,1,4,5,6], k = 2
        ## out: [1,2],[1,2,1],[2,1],[1,4], [4,5], [5,6] -> 6
        arrays = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if len(set(nums[i:j])) == k:
                    arrays.append(nums[i:j])


        return len(arrays)
