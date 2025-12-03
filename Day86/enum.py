from enum import Enum

class Example(Enum):
    A = 10
    B = 11
    C = 12

# Print values
print(f"A = {Example.A.value}")
print(f"B = {Example.B.value}")
print(f"C = {Example.C.value}")