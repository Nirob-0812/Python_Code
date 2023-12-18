import numpy as np
import math

def main():
    print("Advanced Scientific Calculator")
    while True:
        print("\nOperations:")
        print("1. Addition")

        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Natural Logarithm")
        print("8. Trigonometric Functions")
        print("9. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            square_root()
        elif choice == '6':
            exponentiate()
        elif choice == '7':
            natural_logarithm()
        elif choice == '8':
            trig_functions()
        elif choice == '9':
            print("Calculator is quitting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result: ", result)

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("Result: ", result)

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Result: ", result)

def divide():
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result: ", result)

def square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Square root of a negative number is not defined.")
    else:
        result = np.sqrt(num)
        print("Result: ", result)

def exponentiate():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = np.power(base, exponent)
    print("Result: ", result)

def natural_logarithm():
    num = float(input("Enter a positive number: "))
    if num <= 0:
        print("Error: Natural logarithm is only defined for positive numbers.")
    else:
        result = np.log(num)
        print("Natural Logarithm: ", result)

def trig_functions():
    print("\nTrigonometric Functions:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    choice = input("Enter your choice (1/2/3): ")
    angle = float(input("Enter the angle in degrees: "))
    angle_rad = math.radians(angle)

    if choice == '1':
        result = np.sin(angle_rad)
        print("Sine(", angle, " degrees) = ", result)
    elif choice == '2':
        result = np.cos(angle_rad)
        print("Cosine(", angle, " degrees) = ", result)
    elif choice == '3':
        if math.cos(angle_rad) == 0:
            print("Error: Tangent is undefined for this angle.")
        else:
            result = np.tan(angle_rad)
            print("Tangent(", angle, " degrees) = ", result)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()