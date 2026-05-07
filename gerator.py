def my_gen():
    yield "Apple"  #give one item and pause
    yield "Mango"
    yield "Banana"

g = my_gen()

print(next(g))
print(next(g))
print(next(g))