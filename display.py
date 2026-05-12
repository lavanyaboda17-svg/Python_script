def display(message, header=None):

    def decorator(func):

        def wrapper(self):
            if header:
                print(header)           # prints --- Sort ---

            result = func(self)         # runs bubble_sort 

            print(f"{message} : {result}")  # prints Bubble Sort : [1,3,4,5]
            print()                     # blank line

            return result

        return wrapper
    return decorator