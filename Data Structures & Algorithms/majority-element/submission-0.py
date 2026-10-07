class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol=None
        c=0
        for i in nums:
            if c==0:
                sol=i
            c+=(1 if i==sol else -1)
        return sol