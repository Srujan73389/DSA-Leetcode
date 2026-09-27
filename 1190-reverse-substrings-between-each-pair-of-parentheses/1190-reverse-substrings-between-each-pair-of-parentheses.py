class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""

        for char in s:
            if char == '(':
                stack.append(current)
                current = ""

            elif char == ')':
                prev = stack.pop()
                current = prev + current[::-1]

            else:
                current += char

        return current