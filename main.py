# Factorial using for loop

num = int(input("Enter a number: "))

factorial = 1  # start with 1 because multiplication identity is 1

for i in range(1, num + 1):  # loop from 1 to num
    factorial = factorial * i  # multiply each number to factorial

print("Factorial of", num, "is", factorial)
