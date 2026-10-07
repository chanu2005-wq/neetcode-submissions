class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d1={}
        for i in range(len(nums)):
            if nums[i] in d1 and i-d1[nums[i]]<=k:
                return True
            d1[nums[i]]=i
        return False