class Solution:
    def RunLengthEncoding(self, chars : str) -> str:
        #in: "aabbbc"
        #out: "2a3b1c"
        if len(chars) < 1:
            return ""
        list_count = []
        for i in range(0, len(chars)):
            if chars[i] in " !&#$%-/":
                break
            if i == 0 or chars[i] != chars[i - 1]:
                c_count = 1
                for n in range(1, len(chars)-i):
                    if chars[i] != chars[i + n]:
                        break
                    else:
                        c_count += 1

                list_count.append(str(c_count) + str(chars[i]))
        return print("".join(list_count))