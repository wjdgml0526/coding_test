class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for s in strs :
            # key 검사
            k = ''.join(sorted(s))
            if k not in anag.keys() :
                anag[k] = [s]
            else :
                anag[k].append(s)

        return anag.values()