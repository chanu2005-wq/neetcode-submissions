class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cur=0
        prefixSums={0:1}

        for num in nums:
            cur+=num
            diff=cur-k

            res+=prefixSums.get(diff,0)
            prefixSums[cur]=1+prefixSums.get(cur,0)

        return res
