class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        swap_counter=0
        n=len(nums)
        while True:
            swapped=False
            for i in range(1,n):
                if nums[i-1]>nums[i]:
                    nums[i-1],nums[i]=nums[i],nums[i-1]

                    swapped=True
                    swap_counter+=1
            
            if not swapped:
                break
            n-=1

        return nums