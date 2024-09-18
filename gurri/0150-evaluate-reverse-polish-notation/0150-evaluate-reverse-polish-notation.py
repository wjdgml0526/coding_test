class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens : 
            if token in ["+", "-", "*", "/"] :
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(str(int(eval(n2+token+n1))))
            else : 
                stack.append(token)
            # print(stack)
        return int(stack[0])