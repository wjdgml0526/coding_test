class Solution:
        def isValid(self, s: str) -> bool:

            b_idx = {
                '[': 0,
                ']': 0,
                '(': 1,
                ')': 1,
                '{': 2,
                '}': 2,
            }

            stack = []

            for b in s:
                if b in ['[', '{', '(']:
                    stack.append(b)
                else :
                    if len(stack) == 0 :
                        return False

                    # 현재의 b와 opponent 가 같은 그룹에 있는지
                    opponent_bracket = stack.pop()

                    if b_idx[b] != b_idx[opponent_bracket]:
                        return False

            return True if len(stack) == 0 else False
