class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        for word in strs[1:]:
            i=0
            while i<len(pre) and i<len(word) and pre[i]==word[i]:
                i+=1

            pre=pre[:i]

            if pre=="":
                break

        return pre
