class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = set(['*', '/', '+', '-'])
        for x in tokens:
            if x in opers:
                a = int(stack.pop())
                b = int(stack.pop())
                if x == '*':
                    stack.append(b*a)
                elif x == '/':
                    stack.append(int(b/a))
                elif x == '+':
                    stack.append(b+a)
                else:
                    stack.append(b-a)
            else:
                stack.append(int(x))
        return stack[0]