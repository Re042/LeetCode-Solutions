class Solution:
    def isValid(self, s: str) -> bool:
        pars = {')': '(', '}': '{', ']': '['}
        stack = []
        for x in s:
            if x in pars:
                if not stack:
                    return False
                if stack.pop() != pars[x]:
                    return False
            else:
                stack.append(x)
        if stack:
            return False
        return True