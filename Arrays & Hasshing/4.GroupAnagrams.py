class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hashmap = {}
        for string in strs:
            a= ''.join(sorted(list(string)))
            if a not in hashmap:
                hashmap[a] = []
            hashmap[a].append(string)

        
        return list(hashmap.values())