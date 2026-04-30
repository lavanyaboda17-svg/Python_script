#upper
text = "hello"
print(text.upper())

#lower
text = "LAVANYA"
print(text.lower())

#capitalize
text = "hey good morning"
print(text.capitalize())

#title
text = "hello world python"
print(text.title())

#replace
text = "hello world"
print(text.replace("world","python"))

#split
text = "heyy beautiful girl"
print(text.split())

#join
words = "hello","world"
print("_".join(words))

#strip : removing extra spaces
text = "  hello dear  "
print(text.strip())

#find
text = "heyy guys good morining"
print(text.find("guys"))

#count
text = "Lavanya"
print(text.count("a"))

#startswith (True,Flase)
text = "hello world"
print(text.startswith("hello"))

#endswith(True,Flase)
text = "hello world"
print(text.endswith("world"))

#len 
text = "Lavanya"
print(len(text))

#isalpha : checking if the string contains only letters (A to Z)
text = "python"
print(text.isalpha())

#isdigit (True,False)
text = "1234"
print(text.isdigit())

#isalnum : checking if the string has only alphabets and numbers.
text = "abc123"
print(text.isalnum())

#swapcase():This changes capital letters to small letters 
# and small letters to capital letters.
text = "Hello World"
print(text.swapcase())
