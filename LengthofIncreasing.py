from bisect import bisect_left
class Solution:
    def length(self, nums: list) -> int:
        l = len(nums)
        sl = 1
        for n in range(l): #iterate list
            ss_list = [nums[n]] #for each index, start a new list
            for i in range(1, l - n): # iterate subsequent list
                if nums[n] < nums[n+i]: # if subsequent > original index -> add to new list *at ordered position*
                    pos = bisect_left(ss_list, nums[n+i])
                    if pos == len(ss_list):
                        ss_list.append(nums[n+i])
                    else:
                        ss_list[pos] = nums[n+i]
            sl = max(sl, len(ss_list))
        return sl

    def length_dp(self, nums: list) -> int:
        dp = [1] * len(nums) #create dummy list of length nums
        for i in range(1, len(nums)): # iterate list except index 0
            for j in range(i): #iterate up to the index
                if nums[i] > nums[j]: #if n > n-1
                    dp[i] = max(dp[i], dp[j] + 1) #set dp[index] = max(existing dp index, )

        return max(dp)

    def length_bs(self, nums: list) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)

    def length_ss(self, nums: list) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)
    #l = [10,9,2,5,3,4]

