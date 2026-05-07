class Palindrome:
    def __init__(self, word):
        self.word     = word
     

    def palindrome(self):
        return 
    def display(self):
        print("Word    :", self.word)
      
        if self.palindrome():
            print(self.word, "→ IS a Palindrome")
        else:
            print(self.word, "→ is NOT a Palindrome")