
def factorial(num):
    if num < 0:
        print("Negative numbers aren't allowed")
        return -1
    elif num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

number = input("Enter a nuber: ")
print "Factorial of",number,"is",factorial(number)
