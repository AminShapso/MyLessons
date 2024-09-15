"""
The == operator compares the value or equality of two objects
whereas the Python "is" operator checks whether two variables point to the same object in memory.
You can use "is" only for True / False / None statements
Syntax:
if x is not None
if not x == None
and = &
or = |
xor = ^ = return False if equal
"""


my_bool_1 = True
my_bool_2 = False
my_bool_6 = None

if my_bool_1:
    print("my_bool_1")
if my_bool_2:
    print("my_bool_2")
if not 2 == 1:
    print("my_bool_3")
if 2 != 1:
    print("my_bool_4")

my_bool_5 = []
my_bool_5.append([True, True, True])
my_bool_5.append([True, True, False])
my_bool_5.append([True, False, False])
my_bool_5.append([False, False, False])

for mb in my_bool_5:
    print(f"{mb}")
    if mb[0] and mb[1] and mb[2]:
        print("AND")
    if mb[0] or mb[1] or mb[2]:
        print("OR")
    if all(mb):
        print("ALL")
    if any(mb):
        print("ANY")

if my_bool_6 is None:
    print("my_bool_6")

my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]
my_list_3 = my_list_1

if my_list_1 == my_list_2:
    print("my_list_1 == my_list_2")
if my_list_1 is my_list_2:
    print("my_list_1 is my_list_2")
if my_list_1 == my_list_3:
    print("my_list_1 == my_list_3")
if my_list_1 is my_list_3:
    print("my_list_1 is my_list_3")

