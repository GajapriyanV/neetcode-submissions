class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        charCount1 = [0] * 26
        charCount2 = [0] * 26

        # Build counts for s1 and the first window of s2
        for i in range(len(s1)):
            charCount1[ord(s1[i]) - ord("a")] += 1
            charCount2[ord(s2[i]) - ord("a")] += 1

        if charCount1 == charCount2:
            return True

        l = 0

        # Slide the fixed-size window through s2
        for r in range(len(s1), len(s2)):
            # Add the new character entering the window
            charCount2[ord(s2[r]) - ord("a")] += 1

            # Remove the old character leaving the window
            charCount2[ord(s2[l]) - ord("a")] -= 1
            l += 1

            if charCount1 == charCount2:
                return True

        return False