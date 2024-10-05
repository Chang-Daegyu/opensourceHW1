
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # 최종 선택된 수정

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The sum is: {add(num1, num2)}")
print(f"The difference is: {subtract(num1, num2)}")
print(f"The product is: {multiply(num1, num2)}")
print(f"The quotient is: {divide(num1, num2)}")
