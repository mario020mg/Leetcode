class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapa={}
        for i in range (len(nums)):
            if (target - nums[i]) in mapa:
                return [mapa[target - nums[i]], i]
            
            mapa[nums[i]] = i
        
        return []
        