from enum import Enum

# Define enum for user roles
class Role(Enum):
    ADMIN = 1
    USER = 2
    GUEST = 3

# Example: set role to GUEST
r = Role.GUEST

# Display message based on role
if r == Role.ADMIN:
    print("Welcome Admin!")
elif r == Role.USER:
    print("Welcome User!")
elif r == Role.GUEST:
    print("Welcome Guest!")