class Solution:
    def RunLengthEncoding(self, chars : str) -> str:
        #in: "aabbbc"
        #out: "2a3b1c"

        if len(chars) < 1:
            return ""

        list_count = []
        i = 0
        while i < len(chars):
            if chars[i] in " !&#$%-/":
                break
            if i == 0 or chars[i] != chars[i - 1]:
                c_count = 1
                print(c_count, i)
                if i == len(chars) -1:
                    c_count = 1
                else:
                    while chars[i] == chars[i + c_count - 1]:
                        c_count += 1
                list_count.append(str(c_count))
                list_count.append(chars[i])
            i += 1
        return print("".join(list_count))