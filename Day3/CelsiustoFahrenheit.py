# Program to convert Celsius to Fahrenheit

# Step 1: Input
celsius = float(input("Enter temperature in Celsius: "))

# Step 2: Conversion
fahrenheit = (celsius * 9/5) + 32

# Step 3: Output
print("Fahrenheit =", int(fahrenheit) if fahrenheit.is_integer() else round(fahrenheit, 2))