class Solution:
    def combinations(self, amount: int, coins: list) -> int:
        # coins = [1,2,5]
        # amount = 5
        [1,1,1,1,1]
        [1,2,2]
        [5]
        [1,1,1,2]
        sub_amount = 0

        while sub_amount < amount:
            for i in range(len(coins)):
                sub_amount += coins[i]

        c = 0
        for i in range(len(coins)):
            if i == amount:
                c +=1
            elif sub_amount < amount:
                sub_amount += coins[i]
        return c