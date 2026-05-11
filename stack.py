from display import display


class ValidParentheses:
    def __init__(self, s):
        self.s = s

    @display("Valid Parentheses", header="Parentheses Check")
    def is_valid(self):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in self.s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack.pop() != pairs[char]:
                    return f"{self.s} is NOT Valid"

        if not stack:
            return f"{self.s} is Valid"
        else:
            return f"{self.s} is NOT Valid"