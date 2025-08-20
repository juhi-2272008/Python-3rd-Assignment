#Program to find a Factorial of a number using Recursion

def factorial(num):
    if num == 0 or  num ==1:
        return 1
    else:
        return num * factorial(num-1)
    
number = int(input("Enter the number: "))
fact = factorial(number)
print(f"Factorial of {number} is: {fact}")
