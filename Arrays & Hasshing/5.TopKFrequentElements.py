# Given an integer array nums and an integer k, return the k 
# most frequent elements. You may return the answer in any order.
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### Solution 1   
        while len(set(nums)) != k :
            for value in set(nums):
                if value in nums:
                    nums.remove(value)
               
        return set(nums)         
    
        ### Solution 2:
        counter = Counter(nums)
        most_common = counter.most_common(k)
        ans = [elem[0] for elem in most_common]
        return ans

        
       
    

                

        
        
        