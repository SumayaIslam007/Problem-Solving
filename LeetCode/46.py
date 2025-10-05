class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        if len(nums)==2:
            return [nums,nums[::-1]]
        else:
            last=nums[-1]
            ans=[]
            for perm in self.permute(nums[:-1]):
                for i in range(len(perm)+1):
                    temp =list(perm)
                    temp.insert(i,last)
                    ans.append(temp)
            return ans



        