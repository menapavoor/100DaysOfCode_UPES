# Program to implement a basic calculator

# Step 1: Input
a, b, op = input("Enter two numbers and an operator (+, -, *, /, %): ").split()
a = int(a)
b = int(b)

# Step 2: Dictionary mapping
operations = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a // b if b != 0 else "Division by zero error",
    '%': a % b if b != 0 else "Division by zero error"
}

# Step 3: Output
print(operations.get(op, "Invalid operator"))
