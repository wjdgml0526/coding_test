class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = list(s)
        arr_t = list(t)

        arr_s.sort()
        arr_t.sort()
        
        print(''.join(arr_s))
        print(''.join(arr_t))

        return  arr_s == arr_t
        