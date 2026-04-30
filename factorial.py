#FACTORIAL
def factorial(n):
    if n < 0:
        print("negative number don't have factorial")
        return
    elif n != int(n):
        print("Decimal number don't have factorial")
        return
    elif n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    

