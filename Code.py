class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d1 = {}
        for x in s1:
            d1[x] = d1.get(x, 0) + 1

        d2 = {}
        for i in range(len(s2)):
            d2[s2[i]] = d2.get(s2[i], 0) + 1
            if i >= len(s1):
                d2[s2[i - len(s1)]] -= 1
                if d2[s2[i - len(s1)]] == 0:
                    del d2[s2[i - len(s1)]]
            if i >= len(s1) - 1 and d1 == d2:
                return True

        return False
