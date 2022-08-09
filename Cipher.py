class Solution:
    def rotate_chr_nm(self, string: str, k: int) -> str:

        c = string.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for n in range(len(string)):
            if c[n] not in alphabet:
                break
            rotated_pos = ord(c[n]) + k
            # If the rotation is inside the alphabet
            if rotated_pos <= ord(alphabet[-1]):
                c[n] = chr(rotated_pos)
            # If the rotation goes beyond the alphabet
            else:
                c[n] = chr(rotated_pos - len(alphabet))
        return c

    def rotate_chr(self, string : str, k : int) -> str:
        def __rotate(string, k):
            c = string.lower()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            # Keep punctuation and whitespace
            if c not in alphabet:
                return c
            rotated_pos = ord(c) + k
            # If the rotation is inside the alphabet
            if rotated_pos <= ord(alphabet[-1]):
                return chr(rotated_pos)
            # If the rotation goes beyond the alphabet
            return chr(rotated_pos - len(alphabet))
        return ''.join(list(map(__rotate, string)))