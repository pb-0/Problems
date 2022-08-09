class Solution:
    def merge_the_tools(self, string: str, k: int) -> list:
        # your code goes here
        i = 0
        gs = []
        while i < len(string):
            ss = []
            ss.append(string[i])
            for h in range(1, k):
                if string[i + h] not in string[i: i + h]:
                    ss.append(string[i + h])
            gs.append(ss)
            i += k

        return gs