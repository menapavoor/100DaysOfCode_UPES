from enum import Enum

class Month(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12

# Example: set month to FEB
m = Month.FEB

if m == Month.JAN:
    print("31 days")
elif m == Month.FEB:
    print("28 or 29 days")
elif m == Month.MAR:
    print("31 days")
elif m == Month.APR:
    print("30 days")
elif m == Month.MAY:
    print("31 days")
elif m == Month.JUN:
    print("30 days")
elif m == Month.JUL:
    print("31 days")
elif m == Month.AUG:
    print("31 days")
elif m == Month.SEP:
    print("30 days")
elif m == Month.OCT:
    print("31 days")
elif m == Month.NOV:
    print("30 days")
elif m == Month.DEC:
    print("31 days")