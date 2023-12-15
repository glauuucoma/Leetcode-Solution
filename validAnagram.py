    # def isAnagram(s: str, t:str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     countS, countT = {}, {}

    #     for i in range(len(s)):
    #         countS[s[i]] = 1 + countS.get(s[i], 0)
    #         countT[t[i]] = 1 + countT.get(t[i], 0)
    #     for c in countS:
    #         if countS[c] != countS.get(c, 0)
    #             return False

    #     return True

    # # Solution 2
    # def isAnagram2(s: str, t:str) -> bool:
    #     return sorted(s) == sorted(t)

try:
    print([1,2,3,4].index(0))
except:
    pass
