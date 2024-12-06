#acpsquarerootl4
number = float(input("Enter a number that u want to find out the square root for:"))

if number >= 0:
    square_root = number ** 0.5
    print(f"The square root of {number} is {square_root}")
else:
    print("Square root of a negative number is not real.")