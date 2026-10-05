class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                top=stack.pop()
                A=max(2*top,1)
                B=stack.pop()
                stack.append(A+B)
        return stack.pop()
        