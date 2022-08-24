class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

       #test caseses
        #5
# 7
# [2,2]
# [4,4]
# [[3,0], [2,5]]
# 1
# 3
# [0,1]
# [0,0]
# [[0,2]]
        # store when a nut had been placed
        nuts_placed = [0] * len(nuts)

        return self.dfs(squirrel, tree, nuts, nuts_placed)

    def dfs(self, squirrel, tree, nuts, nuts_placed):
        # recalc distance at each new squirell location
        # exit if all nuts placed
        moves = 0
        d = {}
        print(nuts_placed)
        for n in range(len(nuts)):
            if not nuts_placed[n]:
                distance = abs(nuts[n][0] - squirrel[0]) + abs(nuts[n][1] - squirrel[1]) + abs(
                    tree[0] - nuts[n][0]) + abs(tree[1] - nuts[n][1])
                d[n] = distance
        print(d)
        # go to closest nut from squirel location (in case of tie, pick first)
        next_nut = [nuts[i] for i in d if d[i] == min(d.values())][0]
        print(next_nut)

        # add tree distance when nut if found - squirel always goes to tree
        moves = d[nuts.index(next_nut)]
        # + abs(next_nut[0] - tree[0]) + abs(next_nut[1] - tree[1])

        # update nut to placed
        nuts_placed[nuts.index(next_nut)] = 1

        if not min(nuts_placed):
            moves += self.dfs(tree, tree, nuts, nuts_placed)  # update squirrel location

        return moves