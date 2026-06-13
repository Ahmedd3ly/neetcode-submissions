class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        countWindow = {}
        have, need = 0, len(countT)

        l = 0
        resLength = float('infinity')
        subl, subr = 0, 0 

        for r in range(len(s)):
            char = s[r]
            countWindow[char] = 1 + countWindow.get(char, 0)

            if char in countT and countWindow[char] == countT[char]:
                have += 1

            while have == need:
                windowSize = (r - l) + 1
                if windowSize < resLength:
                    resLength  = windowSize
                    subl, subr = l, r + 1
                
                char = s[l]
                countWindow[char] -= 1

                if char in countT and countWindow[char] < countT[char]:
                    have -= 1

                l += 1

        return s[subl : subr] if resLength != float('infinity') else "" 
