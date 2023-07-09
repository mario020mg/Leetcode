

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        for  token in tokens:
            
            if token in "+-*/" :
                val=eval(stack[-2]+token+stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(val)))
            else:
                stack.append(token)
                
            
        return int(stack[0])
