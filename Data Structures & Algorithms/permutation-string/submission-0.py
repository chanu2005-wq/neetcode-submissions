class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_co = [0] * 26
        wi_co = [0] * 26

        for ch in s1:
            s1_co[ord(ch) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):

            wi_co[ord(s2[r]) - ord('a')] += 1

        # Maintain fixed window size
            if r - l + 1 > len(s1):

                wi_co[ord(s2[l]) - ord('a')] -= 1
                l += 1

        # Compare frequencies
            if s1_co == wi_co:
                return True

        return False