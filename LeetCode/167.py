class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i in range (0,len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target-numbers[i]],i+1]
            else:
                dic[numbers[i]]=i+1