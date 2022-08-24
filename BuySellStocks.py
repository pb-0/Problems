class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # buy/sell

        # local minima plus first day
        local_min = [(i, prices[i]) for i in range(len(prices) - 1) if
                     i == 0 or prices[i] < prices[i + 1] and prices[i] <= prices[i - 1]]

        # local maxima plus last day
        local_max = [(i, prices[i]) for i in range(1, len(prices)) if
                     i == len(prices) - 1 or prices[i] > prices[i + 1] and prices[i] > prices[i - 1]]

        all_points = local_min + local_max
        all_points.sort(key=lambda x: x[0])

        dp = [[]] * k
        self.dfs(all_points, dp, k)

        print(dp)

    def dfs(self, all_points, dp, k):
        j = 0
        print(dp)
        for i in range(len(all_points) - 1):
            for h in range(1, len(all_points) - i):
                print(i, h, j)
                if (i, h) not in dp[j] and all_points[i][1] < all_points[i + h][1]:
                    dp[j].append((i, h))
                    j += 1
                    if j == k:
                        self.dfs(all_points, dp, k)
                    break

