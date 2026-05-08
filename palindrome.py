from display import display

class Palindrome:
    def __init__(self, word):
        self.word = word

    @display("Palindrome Check",header="Palindrome")
    def palindrome(self):
        if self.word == self.word[::-1]:
            return f"{self.word} is a Palindrome"
        else:
            return f"{self.word} is NOT a Palindrome"