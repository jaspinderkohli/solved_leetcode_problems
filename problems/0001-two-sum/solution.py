class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
            inp = [2,7,11,15]
            target = 9

            if 9-2 = 7 in imp return 2 and 7

        '''

        dic = {

        }
        for i,x in enumerate(nums):
            val = target - x
            if val in dic:
                return [i, dic[val]]
            dic[x] = i
        
        
