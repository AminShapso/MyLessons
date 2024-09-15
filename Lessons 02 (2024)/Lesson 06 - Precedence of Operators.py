# Taken from:
# https://pythonflood.com/python-operator-precedence-simplifying-complex-expressions-22eb46b334

# The order for Logical operations:
# 1. NOT → right to left
# 2. AND → left to right
# 3. OR → left to right

def this_is_just_a_number(number):
    print("this_is_just_a_number()")
    return number

print(f"{True and False or False = }")
print(f"{True or False and False = }")
print(f"{(True or False) and False = }")
print()

print(f"{not False and False = }")
print(f"{not (False and False) = }")
print()

if this_is_just_a_number(1):
    print("yes")

a = 0 + 0
if a + 1 == 1:
    print("yes")
