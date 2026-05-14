# regex.py

from display import display

class Regex:
    def __init__(self, s, p=""):
        self.s = s
        self.p = p

    def match(self):
        s = self.s
        if "@" not in s:          result = False
        elif "." not in s:        result = False
        else:
            pos     = s.index("@")
            dot_pos = s.index(".", pos)
            if pos == 0:              result = False
            elif dot_pos == pos + 1:  result = False
            elif dot_pos == len(s)-1: result = False
            else:                     result = True

        print(f"{s} : {result}")
        return result

    @display("Starts With", header="Regex")
    def starts_with(self):
        return self.s.startswith(self.p)

    @display("Ends With", header="Regex")
    def ends_with(self):
        return self.s.endswith(self.p)

    @display("Contains", header="Regex")
    def contains(self):
        return self.p in self.s

    @display("Count Matches", header="Regex")
    def count_matches(self):
        return self.s.count(self.p)

    @display("Is Valid Pattern", header="Regex")
    def is_valid_pattern(self):
        if self.p == "":       return False
        if self.p[0] == "*":   return False
        if "**" in self.p:     return False
        return True