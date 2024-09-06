class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        strs_dict = {}
        for string in strs:
            sorted_string = str(sorted(string))
            try:
                strs_dict[sorted_string].append(string)
            except:
                strs_dict[sorted_string] = [string]
        
        return strs_dict.values()
        