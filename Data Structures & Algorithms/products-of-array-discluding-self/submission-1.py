class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l=1
        prod_r=1
        prod_right=[]
        prod_left=[]

        for i in range(1,len(nums)):
            prod_l*=nums[i-1]
            prod_left.append(prod_l)
        prod_left.insert(0,1)

        for j in range(len(nums)-2,-1,-1):
            prod_r*=nums[j+1]
            prod_right.insert(0,prod_r)
        prod_right.append(1)

        prod=[]
        for i in range(len(nums)):
            prod.append(prod_left[i]*prod_right[i])
        return prod 
