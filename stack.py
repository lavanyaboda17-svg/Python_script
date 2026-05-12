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
                stack.append(char)  #push it
            elif char in ')]}':
                if not stack or stack.pop() != pairs[char]:
                    return f"{self.s} is NOT Valid" #empty or wrong match : fail

        if not stack:
            return f"{self.s} is Valid"  #All brackets were matched
        else:
            return f"{self.s} is NOT Valid"  # Some openers were never closed (e.g. "((")