class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        else:
            last = nums[-1]
            ans=[]
            for perm in self.permuteUnique(nums[:-1]):
                for i in range (len(perm)+1):
                    temp = list(perm)
                    temp.insert(i,last)
                    ans.append(temp)
            return  list(map(list,set(map(tuple,ans))))
            



        