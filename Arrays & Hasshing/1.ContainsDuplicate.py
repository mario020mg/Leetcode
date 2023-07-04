class Solution(object):
    def containsDuplicate(self, nums):
        """"
        :type nums: List[int]
        :rtype: bool
        """
        newSet = set(nums)
        if len(nums) == len(newSet):
            return False
        return True
       