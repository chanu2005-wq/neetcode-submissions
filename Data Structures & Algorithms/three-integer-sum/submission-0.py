class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        num=nums
        num.sort()
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:
                continue
            target=-num[i]
            left=i+1
            right=len(num)-1
            while left<right:
                sum=num[left]+num[right]
                if sum==target:
                    res.append([num[i],num[left],num[right]])
                    while left<right and num[left]==num[left+1]:
                        left+=1
                    while left<right and num[right]==num[right-1]:
                        right-=1
                if sum<target:
                    left+=1
                else:
                    right-=1
            
        return res
