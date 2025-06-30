def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y

def power(x,y):
    return x**y

#if __name__ == "__main__":
    print("Welcome to the calculator app!")
    print("Available operations: add, subtract, multiply, divide, power")
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Enter operation: ").strip().lower()

    if operation == "+":
        print(f"Result: {add(x, y)}")
    elif operation == "-":
        print(f"Result: {subtract(x, y)}")
    elif operation == "*":
        print(f"Result: {multiply(x, y)}")
    elif operation == "/":
        try:
            print(f"Result: {divide(x, y)}")
        except ValueError as e:
            print(e)
    elif operation == "**":
        print(f"Result: {power(x, y)}")
    else:
        print("Invalid operation")
    print("Thank you for using the calculator app!")
    print("Exiting the calculator app.")
    print("Goodbye!")

