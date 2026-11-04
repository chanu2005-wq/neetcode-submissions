class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        tar=skill[0]+skill[-1]
        ans=0
        for i in range(len(skill)//2):
            a,b=skill[i],skill[-1-i]
            if a+b!=tar:return -1
            ans+=a*b
        return ans
