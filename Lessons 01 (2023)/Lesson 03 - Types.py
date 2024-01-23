import math

all_types = []
my_dict = dict()

all_types.append("Hello World")   # str
all_types.append(20)   # int
all_types.append(20.5)   # float
all_types.append(range(6))   # range
all_types.append(True)   # bool
all_types.append(["apple", "banana", "cherry"])   # list
all_types.append({"name": "John", "age": 36})   # dict
all_types.append(("apple", "banana", "cherry"))   # tuple = like list but immutable
all_types.append(10+1j)   # complex
all_types.append(None)   # NoneType
for (i, x) in enumerate(all_types):
    print(f"type of index {i} is {type(x)}")
    if x is None:
        print(f"value at index = {i} is a None type")
print()

my_dict['name'] = 'amin'
my_dict['age'] = 14
my_dict[666] = 'yes please'
for i, (key, value) in enumerate(my_dict.items()):
    print(f"my_dict index {i} is: key = {key} and value = {value}")

print()
print(f'math.floor(20.5) = {math.floor(20.5)}')
print(f'math.ceil(20.5) = {math.ceil(20.5)}')
print(f'round(20.5) = {round(20.5)}')
print(f'round(20.501) = {round(20.501)}')
print(f'int(20.99999) = {int(20.99999)}')

print()
int_a = 5
int_b = int_a
print(f"{int_a = }")
print(f"{int_b = }")
int_a += 5
print(f"{int_a = }")
print(f"{int_b = }")

list_a = [1, 2, 3, 4, 5]
list_b = list_a
print(f"{list_a = }")
print(f"{list_b = }")
list_a.reverse()
print(f"{list_a = }")
print(f"{list_b = }")

list_c = [1, 2, 3, 4, 5]
list_d = list_c.copy()
print(f"{list_c = }")
print(f"{list_d = }")
list_c.reverse()
print(f"{list_c = }")
print(f"{list_d = }")

string_a = "[1, 2, 3, 4, 5]"
string_b = string_a
print(f"{string_a = }")
print(f"{string_b = }")
string_a = string_a.replace("[","(").replace("]", ")")
print(f"{string_a = }")
print(f"{string_b = }")

