class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: 
            return False

        countS1 = {}
        for char in s1:
            countS1[char] = 1 + countS1.get(char, 0)

        l = 0
        countWindow = {}
        have, need = 0, len(countS1)

        for r in range(len(s2)):
            right_char = s2[r]
            countWindow[right_char] = 1 + countWindow.get(right_char, 0)

            if right_char in countS1 and countWindow[right_char] == countS1[right_char]:
                have += 1

            if (r - l) + 1 > n1:
                left_char = s2[l]

                if left_char in countS1 and countWindow[left_char] == countS1[left_char]:
                    have -= 1
                
                countWindow[left_char] -= 1
                l += 1

            if have == need:
                return True

        return False