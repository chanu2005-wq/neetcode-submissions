class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):

        # add current character
            count[s[right]] = count.get(s[right], 0) + 1

        # track highest frequency in window
            max_freq = max(max_freq, count[s[right]])

        # current window length
            window_len = right - left + 1

        # invalid window
            if window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1

        # update answer
            result = max(result, right - left + 1)

        return result