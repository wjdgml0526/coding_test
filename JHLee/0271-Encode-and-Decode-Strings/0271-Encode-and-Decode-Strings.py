class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += '\n' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        for string in s:
            if string == '\n':
                result.append('')
            else:
                result[-1] += string
        return result
