from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        print(digits)
        for i in range(30):
            powerOfTwo = str(1 << i)
            print(powerOfTwo)
            if digits == Counter(powerOfTwo):
                return True
        return False