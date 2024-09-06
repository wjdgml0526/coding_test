class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}

        for s in strs:
            v = ''.join(sorted(s))
            if v in result.keys():
                result[v].append(s)
            else:
                result[v] = [s]

        return result.values()

